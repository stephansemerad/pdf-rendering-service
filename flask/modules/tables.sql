
CREATE TABLE IF NOT EXISTS api_keys
(
    api_key_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    api_key TEXT NOT NULL,
    status TEXT NOT NULL,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP 
)
;
CREATE TABLE IF NOT EXISTS pdfs
(
    pdf_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    ip_address TEXT NOT NULL,
    status TEXT NOT NULL,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
;
CREATE TABLE IF NOT EXISTS imgs
(
    pdf_id INTEGER NOT NULL,
    img_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    ip_address TEXT NOT NULL,
    status TEXT NOT NULL,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
;
insert into api_keys (api_key, status) 
select 'y42WTaddY2pt7m90tqKW', 'active' 
where not exists ( select * from api_keys where api_key = 'y42WTaddY2pt7m90tqKW');

