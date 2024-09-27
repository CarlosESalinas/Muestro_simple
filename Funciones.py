import statistics
import math

class Estadisticas:
    def __init__(self, datos):
        self.datos = datos
    
    def aleatorio_simple(self, datos, n: int):
        """
        Realiza un muestreo aleatorio simple
        Parametros:
            datos: list | datos de la poblacion
            n: int | tamaño de la muestra
        Return:
            muestra list | muestra aleatoria simple
        """
        muestra = datos.sample(n=n)
        return muestra
    
    def media_sin_correcion(self, datos, col_numerica, z: float, presicion: int):
        """
        Calcula la media de una muestra sin correcion
        Parametros:
            datos: list | datos de la muestra
            col_numerica: list | columna numerica de la muestra
            z: float | valor de z
        Return: 
            n0 float | media sin correcion
        """
        s = statistics.stdev(col_numerica)
        n0 = (z**2 * s**2) / presicion**2
        return round(n0,2)
    
    def media_con_correcion(self, datos, n0: float):
        """
        Calcula la media de una muestra con correcion
        Parametros:
            datos: list | datos de la muestra
            n0: float | valor de la media sin correcion
        Return: 
            n float | media con correcion
        """
        n = n0 / (1 + n0 / len(datos))
        return round(n,2)
    
        
    def intervalo_confianza(self, datos, n : int, col_numerica, z: float):
        """
        Calcula el intervalo de confianza de la muestra final
        Parametros:
            datos: list | datos de la muestra
            n: int | tamaño de la muestra final
            col_numerica: list | muestra final
            z: float | valor de z
        Return:
            intervalos: list | intervalos de confianza
        """
        s = statistics.stdev(col_numerica)
        Error_estandar = math.sqrt((1-(n/len(datos))) * (s**2) / n)
        Media_muestral = col_numerica.mean()
        Limite_inferior, Limite_superior = round(Media_muestral - z * Error_estandar, 2), round(Media_muestral + z * Error_estandar, 2)
        return round(Limite_inferior,3), round(Limite_superior, 3)


    def total_estimado(self, datos, col_numerica: float):
        """
        Calcula el total estimado de la poblacion
        Parametros:
            datos: list | datos de la muestra
            media_estimada: float | media estimada de la muestra final
        Return:
            total: float | total estimado
        """
        total_estimado = len(datos) * col_numerica.mean()
        return round(total_estimado,3)      
    
    def intervalo_de_confianza_total(self, datos, total_estimado, col_numerica: float, z: float):
        """
        Calcula el intervalo de confianza del total estimado
        Parametros:
            datos: list | datos de la muestra
            total_estimado: float | total estimado
            z: float | valor de z
        Return:
            Limite_inferior, Limite_superior: float | intervalo de confianza
        """
        Varianza_total = len(datos)**2 * statistics.variance(col_numerica)
        Error_estandar_total = math.sqrt(Varianza_total)
        Limite_inferior, Limite_superior = total_estimado - z * Error_estandar_total,total_estimado + z * Error_estandar_total
        return round(Limite_inferior,2), round(Limite_superior,2)
    
    
    def proporcion_poblacion(self, a:int, n:int):
        """
        Calcula la proporcion de la poblacion
        Parametros:
            datos: list | datos de la poblacion
            a: int | cantidad de elementos de interes
            n: int | tamaño de la muestra final
        Return:
            proporcion: float | proporcion de la poblacion
        """
        proporcion = a / n 
        return round(proporcion,2)
    
    def total_estimado_proporcion(self,datos,  p: float):
        """
        Calcula el total estimado de la proporcion
        Parametros:
            datos: list | datos de la poblacion
            p: float | proporcion de la poblacion
        Return:
            total_estimado: float | total estimado
        """
        N = len(datos)
        total_estimado_proporcion = p * N
        return round(total_estimado_proporcion,2)
    
    def intervalo_de_confianza_prop(self, datos, p: float, n: int, z:float, total_esti_propor: float):
        """
        Calcula la varianza de la proporcion
        Parametros:
            datos: list | datos de la poblacion
            p: float | proporcion de la poblacion
            n: int | tamaño de la muestra final
            z: float | valor de z
            total_esti_propor: float | total estimado de la proporcion
        Return:
            var_proporcion: float | varianza de la proporcion
        """
        q = 1 - p
        N = len(datos)
        var_total_estima_propor = N*(N-n)/(n-1)*p*q
        Ee_standar_proporcion = math.sqrt(var_total_estima_propor)
        Limite_inferior_prop, Limite_superior_prop = total_esti_propor - z*Ee_standar_proporcion, total_esti_propor + z*Ee_standar_proporcion
        
        return round(Limite_superior_prop, 3), round(Limite_inferior_prop, 3)
        
        