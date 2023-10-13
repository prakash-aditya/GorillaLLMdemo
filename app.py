import openai
import streamlit as st
import subprocess

openai.api_key = "Dosen't matter"
openai.api_base = "http://zanino.millennium.berkeley.edu:8000/v1"

#query gorilla agent server
def get_gorilla_response(task_prompt, model):
    try:
        completion = openai.ChatCompletion.create(
            model = model,
            messages = [{"role": "user", "content": task_prompt}]
        )
        print("Response: ", completion)
        return completion.choices[0].message.content
    except Exception as e:
        print("Sorry, Something went wrong!")

def extract_code_from_output(output):
    code = output.split("code>>>:")[1]
    return code.strip()

def run_generated_code(file_path):
    command = ["python3", file_path]

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            st.success("Generated code executed successfully")
            st.code(result.stdout, language='python')
        else:
            st.error("Generated code failed to run!")
            st.code(result.stderr, language='bash')
    except Exception as e:
        st.error("Something went wrhong!", e)

st.set_page_config(layout="wide")

def main():
    st.title("Gorilla LLM API Call demo")
    input_promt = st.text_area("Enter your prompt: ")

    option = st.selectbox('Select a model: ', 
                          ('gorilla-7b-hf-v1', 'gorilla-mpt-7b-hf-v0'))
    if st.button("Gorilla Magic"):
        if len(input_promt) > 0:
            col1, col2 = st.columns([1,1])

            with col1:
                if option == 'gorilla-7b-hf-v1':
                    result = get_gorilla_response(task_prompt = input_promt, model = option)
                    st.write(result)
                elif option == 'gorilla-mpt-7b-hf-v0':
                    result = get_gorilla_response(task_prompt=input_promt, model=option)
                    st.write(result)
            with col2:
                if option == 'gorilla-7b-hf-v1':
                    code_result = extract_code_from_output(result)
                    st.subheader("Generated code")
                    st.code(code_result, language='python')

                    file_path = "generated_code_gorilla_7b_hf_v1.py"
                    with open(file_path, 'w') as file:
                        file.write(code_result)

                elif option == 'gorilla-mpt-7b-hf-v0':
                    code_result = extract_code_from_output(result)
                    lines = code_result.split('\\n')
                    for i in range(len(lines) - 1):
                        st.code(lines[i], language='python')
                    
                    file_path = "generated_code_gorilla_mpt_hf_v0.py"
                    with open(file_path, 'w') as file:
                        for i in range(len(lines) - 1):
                            file.write(lines[i].strip().replace('\\"', '"') + '\n')

                run_generated_code(file_path)

if __name__ == "__main__":
    main()