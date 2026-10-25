-- CREATE DATABASE steam_etl 

-- CREATE TABLE IF NOT EXISTS games (
--     appid INT PRIMARY KEY,
--     name TEXT NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS promotions (
--     id SERIAL PRIMARY KEY,
--     appid INT NOT NULL,
--     collection_date DATE NOT NULL,
--     original_price NUMERIC(10,2),
--     final_price NUMERIC(10,2) NOT NULL,
--     discount_percent SMALLINT,
--     expiration TIMESTAMP,
--     CONSTRAINT fk_games
--         FOREIGN KEY(appid)
--         REFERENCES games(appid),
--     CONSTRAINT
--         uq_game_date UNIQUE (appid, collection_date)
-- );

-- INSERT INTO games(appid, name) VALUES(1, 'TESTE');

-- INSERT INTO promotions (appid, collection_date, final_price) 
-- VALUES (1, CURRENT_DATE, 10.00);

-- INSERT INTO promotions (appid, collection_date, final_price) 
-- VALUES (1, CURRENT_DATE, 10.00);

-- INSERT INTO promotions (appid, collection_date, final_price) 
-- VALUES (999, CURRENT_DATE, 10.00);

-- DELETE FROM promotions WHERE appid = 1;
-- DELETE FROM games WHERE appid = 1;