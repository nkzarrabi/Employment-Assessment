CREATE TABLE criteria (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE weights (
    id SERIAL PRIMARY KEY,
    role_id INT NOT NULL,
    criteria_id INT NOT NULL,
    weight DECIMAL(5, 2) NOT NULL,
    FOREIGN KEY (role_id) REFERENCES roles(id),
    FOREIGN KEY (criteria_id) REFERENCES criteria(id)
);

CREATE TABLE core_values (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);
