# Dockerfile, Image, Container
FROM python:3.9

ADD main.py . 

RUN pip install requests simple_term_menu

CMD ["python", "./main.py", "./tax_data.py"]