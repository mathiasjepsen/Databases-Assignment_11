create database MicroShop;
drop table if exists Customer;
create table Customer(
	name VARCHAR(30)
);
drop table if exists Order;
create table Order(
	date VARCHAR(30)
	total INT
	customer INT
);
drop table if exists OrderLine;
create table OrderLine(
	order INT
	product INT
	count INT
	total INT
);
drop table if exists Product;
create table Product(
	name VARCHAR(30)
	price INT
);
