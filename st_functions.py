import streamlit as st
import urllib.parse

def load_css():
    with open("style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

def st_button(icon, url, label, iconsize):
    if icon == 'github':
        button_code = f'''
        <p>
            <a href="{url}" class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width="{iconsize}" height="{iconsize}" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
                    <path d="M0 8.146c0 3.823 2.491 7.066 5.946 8.195.436.082.598-.19.598-.425 0-.209-.008-.76-.012-1.492-2.42.443-2.93-1.17-2.93-1.17-.396-1.002-.966-1.267-.966-1.267-.787-.536-.015-.527.015-.527.871.062 1.33.895 1.33.895.773 1.32 2.026.94 2.52.715.077-.56.3-.938.545-1.155-1.905-.215-3.897-.952-3.897-4.244 0-.94.336-1.71.888-2.31-.09-.215-.384-1.09.083-2.275 0 0 .723-.23 2.367.882.686-.188 1.422-.28 2.154-.283.73.002 1.467.095 2.154.283 1.645-1.113 2.367-.883 2.367-.883.468 1.185.173 2.06.085 2.275.552.6.886 1.37.886 2.31 0 3.302-1.997 4.028-3.91 4.237.307.265.582.791.582 1.587 0 1.147-.01 2.07-.01 2.346 0 .236.16.513.606.425C13.51 15.21 16 11.97 16 8.145 16 3.663 12.418 0 8 0S0 3.663 0 8.146z"/>
                </svg>  
                {label}
            </a>
        </p>'''
    elif icon == 'linkedin':
        button_code = f'''
        <p>
            <a href="{url}" class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width="{iconsize}" height="{iconsize}" fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16">
                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                </svg>
                {label}
            </a>
        </p>'''
    elif icon == 'whatsapp':
        # Botón sin icono
        button_code = f'''
        <p>
            <a href="{url}" class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg aria-hidden="true" focusable="false" data-prefix="fab" data-icon="whatsapp" class="svg-inline--fa fa-whatsapp" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="{iconsize}"  height="{iconsize}">
                    <path fill="currentColor" d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"></path>
            </svg>
                {label}
            </a>
        </p>
        '''
    return st.markdown(button_code, unsafe_allow_html=True)

