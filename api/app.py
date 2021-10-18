from flask import Flask, request, jsonify, render_template, redirect
import os
import urllib.request
from nltk.util import ngrams
import pickle
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

def gen_result(S):
    switch = {
        0: "Non-Plagiarized",
        1: "Lightly Plagiarized",
        2: "Heavily Plagiarized",
        3: "Near-Copy",
    }
    return switch.get(S)


@app.route("/")
@cross_origin()
def index():
    return jsonify("Pong!")


@app.route("/api/test/", methods=["POST"])
@cross_origin()
def test():
    # data = request.get_json()
    # # username = data.get("username")
    # # password = generate_password_hash(data.get("password"))
    # name = data["name"]
    # filedata = request.files["file"]
    # o = filedata.read()
    # print(name)
    # print(0)
    filedata = request.files["file"]
    url = request.form["url"]
    testfile = filedata.read()
    
    

    webUrl = urllib.request.urlopen(url)
    d = webUrl.read()
    data = str(d, "utf-8")
    print("Original is: ",data)
    ori = data.lower()
    testfile = str(testfile,"utf-8")
    testfile = testfile.lower()

    # Calculation of Similar Bigrams
    n_bi = 2

    nb1 = ngrams(ori.split(), n_bi)
    nb2 = ngrams(testfile.split(), n_bi)
    bi1 = []
    bi2 = []
    for grams1 in nb1:
        bi1.append(grams1)

    for grams2 in nb2:
        bi2.append(grams2)

    b_count = 0
    l_b1 = len(bi1)
    l_b2 = len(bi2)
    for i in range(l_b1):
        for j in range(l_b2):
            if bi1[i] == bi2[j]:
                b_count += 1
                break
    b_perc = (b_count) * 100 / (l_b2)
    # Calculation of Similar Trigrams
    n_tri = 3

    nt1 = ngrams(ori.split(), n_tri)
    nt2 = ngrams(testfile.split(), n_tri)
    tri1 = []
    tri2 = []
    for grams1 in nt1:
        tri1.append(grams1)

    for grams2 in nt2:
        tri2.append(grams2)

    t_count = 0
    l_t1 = len(tri1)
    l_t2 = len(tri2)
    for i in range(l_t1):
        for j in range(l_t2):
            if tri1[i] == tri2[j]:
                t_count += 1
                break
    t_perc = (t_count) * 100 / (l_t2)

    # Calculation of Similar Fourgrams
    n_fo = 4

    nfo1 = ngrams(ori.split(), n_fo)
    nfo2 = ngrams(testfile.split(), n_fo)
    fo1 = []
    fo2 = []
    for grams1 in nfo1:
        fo1.append(grams1)

    for grams2 in nfo2:
        fo2.append(grams2)

    fo_count = 0
    l_fo1 = len(fo1)
    l_fo2 = len(fo2)
    for i in range(l_fo1):
        for j in range(l_fo2):
            if fo1[i] == fo2[j]:
                fo_count += 1
                break
    fo_perc = (fo_count) * 100 / (l_fo2)

    # Calculation of Similar Fivegrams
    n_fi = 5

    nfi1 = ngrams(ori.split(), n_fi)
    nfi2 = ngrams(testfile.split(), n_fi)
    fi1 = []
    fi2 = []
    for grams1 in nfi1:
        fi1.append(grams1)

    for grams2 in nfi2:
        fi2.append(grams2)

    fi_count = 0
    l_fi1 = len(fi1)
    l_fi2 = len(fi2)
    for i in range(l_fi1):
        for j in range(l_fi2):
            if fi1[i] == fi2[j]:
                fi_count += 1
                break
    fi_perc = (fi_count) * 100 / (l_fi2)

    Pkl_Filename = "NBModel.pkl"
    with open("NBModel.pkl", "rb") as file:
        NB_Model = pickle.load(file)

    test = [[b_perc, t_perc, fo_perc, fi_perc]]
    print(test)
    r = NB_Model.predict(test)
    print(r[0])
    result = gen_result(r[0])
    print(result)
    if result == "Non-Plagiarized" or result == "Lightly Plagiarized":
        flag = True
    else:
        flag = False

    return jsonify({"status": "success", "result": result, "flag": flag}), 201


@app.after_request
@cross_origin()
def add_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    return response


if __name__ == "__main__":
    app.run(debug=True)
