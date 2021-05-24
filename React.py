import subprocess;
import os;
import time;

app_js='''
    import React from 'react';
    
    const App=()=>(
        return(
            <>
                <h1>React App</h1>
            </>
        )
    )

    export default App;
'''

index_js='''
    import React from 'react';
    import ReactDOM from 'react-dom';
    import App from './App';
    
    ReactDOM.render(
        <React.StrictMode>
            <App/>
        </React.StrictMode>
        ,document.getElementById('root'));
'''

dir_clean=subprocess.Popen('rm -fr *',cwd='src',stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True);
dir_clean_return_code=dir_clean.wait();
time.sleep(5);
os.chdir('src');
print('writing files.....');
app_file=open('App.js','w');
app_file.write(app_js);
app_file.close();
index_file=open('index.js','w');
index_file.write(index_js);
index_file.close();
index_css_file=open('index.css','x');
index_css_file.close();
print('react clean up completed..... \n Happy Hacking');




