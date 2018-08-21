from flask import Flask,Response,abort,jsonify,request,json
import uuid

app=Flask('__name__')

all_questions_list= []
answers=[]

@app.route('/api/v1/questions',methods=['POST'])
def  post_a_question():  
    data = request.get_json()    
    title=data['title']
    body=data['body']
    
    new_question={
            'id': str(uuid.uuid1()),
            'title':title,
            'body':body,
            'user_id': 2
        }
    all_questions_list.append(new_question)
    return jsonify({'question': new_question})

@app.route('/api/v1/questions',methods=['GET'])
def all_questions_getter():
    return jsonify({'questions': all_questions_list})

@app.route('/api/v1/questions/<question_id>',methods=['GET'])
def single_question_getter(question_id):
    for question in all_questions_list:
        if question['id']==question_id:
            return jsonify(question)
    
    return jsonify({ 'error': 'qestion not found' })

@app.route('/api/v1/questions/<question_id>/answer',methods=['POST'])
def post_question(question_id):
    data=request.get_json()
    answer=data['answer']

    new_answer = {
        'id':str(uuid.uuid1()),
        'question_id':question_id,
        'user_id':2,
        'answer':answer
    }
    answers.append(new_answer)
    return jsonify({'message':'Answer succesfully posted'})