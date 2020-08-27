FROM ubuntu
RUN apt update -y
RUN apt install python3 git -y
RUN apt install python3-pip -y
RUN pip3 install flask
RUN pip3 install pymysql
RUN pip3 install cryptography 
RUN rm -fR investguru
RUN git clone https://github.com/gsanthoshkrishna/investguru.git
