sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/hello.py /usr/local/lib/python2.7/hello.py 
#sudo /etc/init.d/gunicorn restart
sudo gunicorn -b 0.0.0.0:8080 hello hello:app &

