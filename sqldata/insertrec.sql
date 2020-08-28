create database murthy;
use murthy;
create table invest_data(name VARCHAR(50),value FLOAT,quantity INTEGER,target FLOAT,tag VARCHAR(50));
insert into invest_data values('test','20.0',4,22,'short');
insert into invest_data values('test2','220.0',24,322,'long');
create table history_data(SYMBOL VARCHAR(20),SERIES VARCHAR(10),OPEN FLOAT,HIGH FLOAT,LOW FLOAT,CLOSE FLOAT,LAST FLOAT,PREVCLOSE FLOAT,TOTTRDQTY FLOAT,TOTTRDVAL FLOAT,TIMESTAMP datetime,TOTALTRADES FLOAT);

