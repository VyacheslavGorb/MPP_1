CREATE DATABASE IF NOT EXISTS todo_list_db;

USE todo_list_db;

CREATE TABLE IF NOT EXISTS users(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    login VARCHAR(60) UNIQUE,
    password CHAR(255)
);

CREATE TABLE IF NOT EXISTS tasks(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT REFERENCES users(id),
    status ENUM('ACTIVE', 'IN_PROGRESS', 'DONE'),
    expected_completeon_date DATE
);

CREATE TABLE IF NOT EXISTS task_files(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    task_id BIGINT REFERENCES tasks(id),
    file_path VARCHAR(256)
);
