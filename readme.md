# 📘 SQL → Markdown генератор

Генерирует документацию по структуре базы данных из `.sql` файла с `CREATE TABLE`.

## 📥 Что нужно

- Docker
- SQL-файл (например `schema.sql`) с описанием структуры таблиц
- Файл должен быть примонтирован в контейнер при запуске

## 🚀 Как использовать

1. Собери Docker-образ

```bash
docker build -t sql-docgen .
```

2. Запусти Docker и укажи название sql файла:

```bash
docker run --rm -v "$PWD":/app sql-docgen schema.sql
```

2. Результат будет находится в tables.md

## Пример

```sql
CREATE TABLE `user` (
    `id` int unsigned NOT NULL AUTO_INCREMENT,
    `username` varchar(255) NOT NULL,
    `email` varchar(255) DEFAULT NULL,
    `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB;

CREATE TABLE `order` (
     `id` bigint NOT NULL AUTO_INCREMENT,
     `user_id` int NOT NULL,
     `total_price` decimal(10,2) DEFAULT 0.00,
     PRIMARY KEY (`id`),
     CONSTRAINT `fk_order_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB;
```

В результате:
# 📋 Документация таблиц на основе `schema-example.sql`

## 🧾 order

| Поле | Тип | Null | По умолчанию | Комментарий |
|------|-----|------|---------------|-------------|
| `id` | bigint | NO | — | — |
| `user_id` | int | NO | — | — |
| `total_price` | decimal(10,2) | YES | 0.00 | — |

**Связи:**
- `user_id` → `user.id`

## 🧾 user

| Поле | Тип | Null | По умолчанию | Комментарий |
|------|-----|------|---------------|-------------|
| `id` | int | NO | — | — |
| `username` | varchar(255) | NO | — | — |
| `email` | varchar(255) | YES | NULL | — |
| `created_at` | datetime | NO | CURRENT_TIMESTAMP | — |


