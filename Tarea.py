def calcular_volumen_arepa():
    print("Bienvenido a la calculadora de volumen de arepa")
    print("\nPor favor ingrese las cantidades (en números):")
    
    try:
        tazas_agua = float(input("Tazas de agua: "))
        tazas_harina = float(input("Tazas de harina PAN: "))
        cdta_sal = float(input("Cucharaditas de sal: "))
        cda_aceite = float(input("Cucharadas de aceite: "))
        
        cdta_agua = tazas_agua * 48
        cdta_harina = tazas_harina * 48
        cdta_aceite = cda_aceite * 3
        
        volumen_total_cdta = cdta_agua + cdta_harina + cdta_sal + cdta_aceite
        volumen_final_cdta = volumen_total_cdta * 0.9
        
        tazas_final = volumen_final_cdta // 48
        cdta_restantes = volumen_final_cdta % 48
        cda_restantes = cdta_restantes // 3
        cdta_restantes = cdta_restantes % 3
        
        print("\nResultados:")
        print(f"Volumen total antes de la cocción: {volumen_total_cdta:.1f} cucharaditas")
        print("Volumen final después de la cocción:")
        if tazas_final > 0:
            print(f"- {int(tazas_final)} taza(s)")
        if cda_restantes > 0:
            print(f"- {int(cda_restantes)} cucharada(s)")
        if cdta_restantes > 0:
            print(f"- {cdta_restantes:.1f} cucharadita(s)")
        print(f"\nPérdida por evaporación: {volumen_total_cdta * 0.1:.1f} cucharaditas")
        
    except ValueError:
        print("Error: Por favor ingrese solo números válidos")

if __name__ == "__main__":
    calcular_volumen_arepa()