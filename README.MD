# Pokédex App

Pokédex App is a Django-based web application that serves as a Pokédex to display information about Pokémon.

## Features

- Display Pokémon details including names, types, base stats, and descriptions.
- Advanced search by Pokémon name or type.
- Responsive and easy-to-navigate user interface.

## Technologies Used

- **Django**: Python web framework for rapid development.
- **Bootstrap**: Front-end framework for design and responsiveness.
- **PostgreSQL**: Relational database for storing Pokémon data.
- **Docker**: Containerization for easier development and deployment environment.
- **Terraform**: Infrastructure as code for managing cloud infrastructure on AWS.

## Prerequisites

- Python 3.8 or later
- Docker
- Docker Compose (optional but recommended for local development)

## Installation and Setup

1. **Clone the repository**

   ```bash
   git clone <URL-of-your-git-repository>
   cd pokedex_app
   ```

2. **Set up environment variables**

   Copy the `.env.example` file to `.env` and modify the environment variables as needed (e.g., database connection settings, API keys, etc.).

3. **Build and run the application**

   Use Docker Compose to build and start the application:

   ```bash
   docker-compose up --build
   ```

   This command will start the Django development server and PostgreSQL database within Docker containers.

4. **Access the application**

   Once the server is running, the application will be accessible at:

   ```
   http://localhost:8000/
   ```

## Contributing

We welcome contributions! Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
