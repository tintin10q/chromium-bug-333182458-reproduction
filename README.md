

# Reproduction steps 

0. Install the python dependencies with `pip install -r requirements.txt` 
1. Add the CA.pem to chrome ([chrome://settings/certificates](chrome://settings/certificates)) as a CA to get a valid https server.
2. Start the webserver with `python https_server.py` the pass phrase is `test`
3. Open [https://localhost:8000](https://localhost:8000)
4. Click the `Subscribe` button
5. Give permissions for push notifications if promted
6. Copy the subscription data into the [push.py](push.py) file (line 9).
7. Run `python push.py` 
8. Observe that the [data property](https://developer.mozilla.org/en-US/docs/Web/API/PushEvent/data) of the push event in the service worker is null
9. Uncomment line 21 in [push.py](push.py) to enable base64 encoding. 
10. Run `python push.py` again, now the data is recieved properly.

> Do not forget to remove the certificate authority again in step 1.

# Firefox

On firefox this does not happen the data is there, both with and without the base64 encoding.

When trying this on firefox you can skip step 1, you can just click `Accept the risk` instead.

