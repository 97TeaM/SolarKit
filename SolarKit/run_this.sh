echo SolarKit

if [ -d "node_modules"]; then
    echo "You have already installed modules";
else
    pip install -r requirements.txt
    npm install -g npm@latest
    npm install -g ddos-stress
    npm update -g
fi
python __main__.py