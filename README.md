# Desafios-Docker-FCCPD


## Sobre o Projeto
Este repositório contém a resolução dos 5 desafios práticos propostos para a avaliação da disciplina. O objetivo foi demonstrar domínio sobre containerização, orquestração, redes e arquitetura de microsserviços utilizando **Docker** e **Docker Compose**.

## Índice dos Desafios

Cada desafio possui sua própria documentação detalhada e instruções de execução dentro de suas respectivas pastas.

| Pasta | Desafio | Tecnologias Principais |
| :--- | :--- | :--- |
| [ /desafio1](./desafio1) | **Containers em Rede**<br>Comunicação entre container Cliente e Servidor via rede bridge. | Nginx, Alpine, Shell Script |
| [ /desafio2](./desafio2) | **Volumes e Persistência**<br>Persistência de dados de um banco SQLite utilizando Bind Mounts. | Python, SQLite, Docker Volumes |
| [ /desafio3](./desafio3) | **Orquestração com Compose**<br>Aplicação completa com Web, Cache e Banco de Dados. | Flask, Redis, PostgreSQL, Docker Compose |
| [ /desafio4](./desafio4) | **Microsserviços HTTP**<br>Comunicação síncrona entre dois microsserviços (API e Frontend). | Python Flask, Requests, API REST |
| [ /desafio5](./desafio5) | **API Gateway**<br>Arquitetura final com Nginx atuando como Proxy Reverso para microsserviços. | Nginx Proxy, Flask, Docker Compose |

---

## Como Executar
Como cada desafio possui requisitos específicos (alguns usam `docker run`, outros `docker-compose`), **por favor navegue até a pasta do desafio desejado** e siga o passo a passo descrito no `README.md` local.

**Exemplo de navegação:**
```bash
cd desafio1
# Leia as instruções no README desta pasta
