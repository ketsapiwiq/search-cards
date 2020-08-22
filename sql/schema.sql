-- create table datas (
--     id serial primary key,
--     number int,
--     description text
-- );

-- insert into datas (number, description) values (
-- 3,
-- 'hello'),
-- (
-- 4,
-- 'goodbye');


create table cards (
    id serial primary key,
    data json
);

insert into cards (data) values ('{"title":
"hello"}');