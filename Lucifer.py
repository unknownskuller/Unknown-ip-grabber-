class colores:
        red="\033[31;1m"
            os.system("clear")
            logo = colores.red + 
                ██  ███▄    █  ██ ▄█▀ ███▄    █  ▒█████   █     █░███▄    █ 
                 ██  ▓██▒ ██ ▀█   █  ██▄█▒  ██ ▀█   █ ▒██▒  ██▒▓█░ █ ░█░██ ▀█   █ 
                 ▓██  ▒██░▓██  ▀█ ██▒▓███▄░ ▓██  ▀█ ██▒▒██░  ██▒▒█░ █ ░█▓██  ▀█ ██▒
                 ▓▓█  ░██░▓██▒  ▐▌██▒▓██ █▄ ▓██▒  ▐▌██▒▒██   ██░░█░ █ ░█▓██▒  ▐▌██▒
                 ▒▒█████▓ ▒██░   ▓██░▒██▒ █▄▒██░   ▓██░░ ████▓▒░░░██▒██▓▒██░   ▓██░
                 ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒ ░ ▒░   ▒ ▒ 
                 ░░▒░ ░ ░ ░ ░░   ░ ▒░░ ░▒ ▒░░ ░░   ░ ▒░  ░ ▒ ▒░   ▒ ░ ░ ░ ░░   ░ ▒░
                  ░░░ ░ ░    ░   ░ ░ ░ ░░ ░    ░   ░ ░ ░ ░ ░ ▒    ░   ░    ░   ░ ░ 
                     ░              ░ ░  ░            ░     ░ ░      ░            ░ 
                                                                                       

try:
  print(logo)

import socket
import requests
import subprocess
from flask import Flask, request, redirect, url_for
red = input("   redirect to :  ")
print("")
app = Flask(name)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
                s.close()
                    return local_ip

                    @app.route('/')
                    def index():
                        return redirect(url_for('get_ip', redirect_to= red))

                        @app.route('/get_ip')
                        def get_ip():
                            
                                local_ip = get_local_ip()
                                    
                                        response = requests.get('https://httpbin.org/ip')
                                            data = response.json()
                                                public_ip = data['origin']

                                                    print("")
                                                        print(f'   [★] -Public IP: {public_ip}')
                                                            print("  ____")
                                                                subprocess.run(['echo', f'   [★] -Local IP: {local_ip}'])
                                                                    print("")

                                                                        redirect_to = request.args.get('redirect_to')
                                                                            if redirect_to:
                                                                                    return redirect(redirect_to)

                                                                                        return f'Local IP: {local_ip}<br>Public IP: {public_ip}'

                                                                                        if name == 'main':
                                                                                            app.run()import socket
                                                                                            import requests
                                                                                            import subprocess
                                                                                            from flask import Flask, request, redirect, url_for
                                                                                            red = input("   redirect to :  ")
                                                                                            print("")
                                                                                            app = Flask(name)

                                                                                            def get_local_ip():
                                                                                                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                                                                                                    s.connect(("8.8.8.8", 80))
                                                                                                        local_ip = s.getsockname()[0]
                                                                                                            s.close()
                                                                                                                return local_ip

                                                                                                                @app.route('/')
                                                                                                                def index():
                                                                                                                    return redirect(url_for('get_ip', redirect_to= red))

                                                                                                                    @app.route('/get_ip')
                                                                                                                    def get_ip():
                                                                                                                        
                                                                                                                            local_ip = get_local_ip()
                                                                                                                                
                                                                                                                                    response = requests.get('https://httpbin.org/ip')
                                                                                                                                        data = response.json()
                                                                                                                                            public_ip = data['origin']

                                                                                                                                                print("")
                                                                                                                                                    print(f'   [★] -Public IP: {public_ip}')
                                                                                                                                                        print("  ____")
                                                                                                                                                            subprocess.run(['echo', f'   [★] -Local IP: {local_ip}'])
                                                                                                                                                                print("")

                                                                                                                                                                    redirect_to = request.args.get('redirect_to')
                                                                                                                                                                        if redirect_to:
                                                                                                                                                                                return redirect(redirect_to)

                                                                                                                                                                                    return f'Local IP: {local_ip}<br>Public IP: {public_ip}'

                                                                                                                                                                                    if name == 'main':
                                                                                                                                                                                        app.run()