import os, json
from flask import Flask, request, abort, jsonify, send_from_directory, render_template
PDF_DIRECTORY = "/api/pdfs"

if not os.path.exists(PDF_DIRECTORY): os.makedirs(PDF_DIRECTORY)
api = Flask(__name__)

@api.route('/', methods=['GET'])
@api.route('/help', methods=['GET'])
def index():
    return render_template('index.html')

#https://resources.infosecinstitute.com/topic/pdf-file-format-basic-structure/
@api.route('/documents',methods = ['POST', 'GET'])
@api.route('/documents/<document_id>',methods = ['POST', 'GET'])
@api.route('/documents/<document_id>/pages/<number>',methods = ['POST', 'GET'])
def documents():
    print(request.headers['api-key'])
    print(request.method)
    if request.method == 'POST':
        print('POST')
        print('\n\n\n data: ')
        print(request.data)
        print(type(request.data))
        data = request.data
        encode_data = encode(request.data)
        data = str(data).split('\n')
        
        print('----------------')
        for i in data:
            print(i)


        print('\n\n\n')
        return jsonify({'name': 'alice',
                        'email': 'alice@outlook.com'})





    # if request.method == 'POST':
    #     user = request.form['nm']
    #     return redirect(url_for('success',name = user))
    # else:
    #     user = request.args.get('nm')
    #     return redirect(url_for('success',name = user))



# @api.route("/files")
# def list_files():
#     print(request.headers['api-key'])
#     """Endpoint to list files on the server."""
#     files = []
#     for filename in os.listdir(PDF_DIRECTORY):
#         path = os.path.join(PDF_DIRECTORY, filename)
#         if os.path.isfile(path):
#             files.append(filename)
#     return jsonify(files)


# @api.route("/files/<path:path>")
# def get_file(path):
#     print(request.headers['api-key'])
#     """Download a file."""
#     return send_from_directory(PDF_DIRECTORY, path, as_attachment=True)


# @api.route("/files/<filename>", methods=["POST"])
# def post_file(filename):
    # print(request.headers['api-key'])

    # """Upload a file."""

    # if "/" in filename:
    #     # Return 400 BAD REQUEST
    #     abort(400, "no subdirectories allowed")

    # with open(os.path.join(PDF_DIRECTORY, filename), "wb") as fp:
    #     fp.write(request.data)

    # # Return 201 CREATED
    # return "", 201


if __name__ == "__main__":
    api.run(debug=True, host='0.0.0.0', port=8080)
    
