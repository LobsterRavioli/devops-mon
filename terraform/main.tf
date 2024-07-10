# Configura il provider AWS e specifica la regione in cui verranno create le risorse.

provider "aws" {
  region = "us-east-1" # specifica la regione desiderata
}

# Crea un cluster ECS chiamato "my-app-cluster".
resource "aws_ecs_cluster" "main" {
  name = "my-app-cluster"
}
# Crea una definizione di task ECS chiamata "my-app-task". La definizione specifica il container "my-app", la sua immagine Docker, CPU e memoria allocate, mappatura delle porte e il ruolo IAM per eseguire il task.
resource "aws_ecs_task_definition" "main" {
  family                   = "my-app-task"
  container_definitions    = jsonencode([
    {
      name      = "my-app"
      image     = "${aws_ecr_repository.main.repository_url}:latest"
      cpu       = 256
      memory    = 512
      essential = true
      portMappings = [
        {
          containerPort = 8000
          hostPort      = 8000
        }
      ]
    }
  ])
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = "256"
  memory                   = "512"
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn
  task_role_arn            = aws_iam_role.ecs_task_execution_role.arn
}

# Crea un servizio ECS chiamato "my-app-service" nel cluster "my-app-cluster". 
# Il servizio utilizza la definizione di task "my-app-task" e avvia un'istanza del task utilizzando Fargate. Specifica anche la configurazione di rete (subnet e gruppi di sicurezza).
resource "aws_ecs_service" "main" {
  name            = "my-app-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.main.arn
  desired_count   = 1
  launch_type     = "FARGATE"
  network_configuration {
    subnets         = aws_subnet.main.*.id
    security_groups = [aws_security_group.main.id]
  }
}

#  Crea un repository Amazon ECR chiamato "my-app-repo" per conservare le immagini Docker.
resource "aws_ecr_repository" "main" {
  name = "my-app-repo"
}
# Crea un ruolo IAM chiamato "ecsTaskExecutionRole" che ECS utilizzerà per eseguire i task. Questo ruolo ha i permessi per essere assunto dai servizi ECS.

resource "aws_iam_role" "ecs_task_execution_role" {
  name = "ecsTaskExecutionRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

#  Crea un gruppo di sicurezza chiamato "my-app-sg" che permette il traffico in entrata sulla porta 8000 (dove l'applicazione è in ascolto) e tutto il traffico in uscita.
resource "aws_security_group" "main" {
  name        = "my-app-sg"
  description = "Security group for my app"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

#  Crea una VPC (Virtual Private Cloud) con un blocco CIDR di "10.0.0.0/16".
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

# Crea due subnet all'interno della VPC "main". Il blocco CIDR di ciascuna subnet è calcolato in base al blocco CIDR della VPC e l'indice della subnet.
resource "aws_subnet" "main" {
  count = 2
  vpc_id = aws_vpc.main.id
  cidr_block = cidrsubnet(aws_vpc.main.cidr_block, 8, count.index)
}
