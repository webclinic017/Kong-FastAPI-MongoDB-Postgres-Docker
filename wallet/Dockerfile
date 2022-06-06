#
FROM python:3.9
# RUN export PYTHONPATH=$PWD
#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./ /code/wallet

#
ENV PYTHONPATH "${PYTHONPATH}:/code/wallet"
ENV DB_URL "mongodb://db/WalletDB"
CMD ["python", "wallet/main.py"]