from flask import Flask,request
from flask import render_template
import openai


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('Converter.html')

@app.route('/')
def Home():
    return render_template('HowToUse.html')

@app.route('/HowToUse')
def HowToUse():
    return render_template('HowToUse.html')

@app.route('/AboutUs')
def AboutUs():
    return render_template('HowToUse.html')

@app.route('/process_data', methods=['POST'])
def main():
    try:
        if request.method=='POST':
            input1=request.form['input1']
            #input2 = "Python"
            #input3 = "Java"
            input2 = request.form['input2']
            input3 = request.form['input3']
            
            result = openai_converter(input1, input2,input3)
            return {"Status":"Success","Converted_code":result}

    except Exception as err:
        print(err)


def openai_converter(doc_text,inp2,inp3):
    openai.api_key = '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'

    #open text file in read mode
    #text_file = open("ChatGptInput.txt", "r")
    #read whole file to a string
    data = doc_text
    #close file
    #text_file.close()
    source_code = inp2
    output_code= inp3

    cmd1="##### Translate this code  from "+source_code+"into "+output_code+"\n"
    cmd2="###" +output_code+"\n"
    cmd3="\n###"+output_code

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=cmd1+cmd2+data+cmd3,
    temperature=0,
    max_tokens=1500,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["###"]
    )
    
    with open("output.txt", "w") as file:
        # Write some text to the file
        #file.write(response.choices[0].text)
        file.write(cmd1+cmd2+data+cmd3)


    result=response.choices[0].text

    return result

if __name__ == '__main__':
    app.run(debug=True)

