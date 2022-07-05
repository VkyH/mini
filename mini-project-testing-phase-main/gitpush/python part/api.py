from flask import Flask, jsonify, request 
import algo

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def checkimage():
  if(request.method == 'GET'):
    img1 = r"C:\Users\Adil Naqvi\Desktop\Projects\Mini Project\face photo classifier\ved.jpeg"
    img2 = r"C:\Users\Adil Naqvi\Desktop\Projects\Mini Project\face photo classifier\ved.jpeg"
    photo_res = algo.fd(img1)
    sig_res = not algo.fd(img2)
    return jsonify({'photo':photo_res,'signature':sig_res})

# driver function
if __name__ == '__main__':

  app.run(debug = True)
