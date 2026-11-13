from fastapi import FastAPI
import subprocess
import db

app = FastAPI(title="Ping API")

db.init_db()

@app.get("/history/{ip}")
def read_pings(ip: str):
    rows = db.get_pings(ip)
    result = []
    for row in rows:
        result.append({"ip": row[0], "status": row[1], "time": str(row[2])})
    
    if not result:
        return {"message": "not found"}

    return result

@app.get("/ping/{ip}")
def ping_host(ip: str):
    
    result = subprocess.run(["ping", "-c", "1", ip], capture_output=True)    
    
    if result.returncode == 0:
        status = "up"
    else: 
        status = "down"
    
    db.save_ping(ip, status)

    return {"ip": ip, "status": status}
