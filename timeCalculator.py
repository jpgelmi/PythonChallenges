def add_time(start, duration):
 
    start_f = start.split(":")
    start_f = start_f[:1] + start_f[1].split(" ")
    duration_f = duration.split(":")

    horas_t = (int(start_f[0]) + int(duration_f[0])) * 60
    minutos_t =  int(start_f[1]) + int(duration_f[1])

    timepo_m = horas_t + minutos_t
    def dias():
        for i in range(30):
            if timepo_m in range(1440 * i, 1440 * (i + 1)):
                apendice = str(i)
                return apendice
        apendice = "más de un mes mas" 
        return apendice
    dias()

    def calcular():
        horas =  int(round(timepo_m/60))
        minutos = timepo_m - horas_t
        if horas > 12:
            print(str(horas) ,":", str(minutos) , "PM")
        else:
            print(str(horas) ,":", str(minutos) , "AM")
        print(dias() , "dias más")
    
    calcular()

add_time("11:06 PM", "13:02")