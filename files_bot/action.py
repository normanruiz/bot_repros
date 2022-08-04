##############################################################################
#                             AVIS SOFTWARE                                  #
#                     (Productos de Software Libre)                          #
#                                                                            #
##############################################################################
#
#  **************************************************************************
#  * El software libre no es una cuestion economica sino una cuestion etica *
#  **************************************************************************
#
# Avis Software es marca registrada.
#
# Este programa es software libre; puede redistribuirlo o modificarlo bajo los
# terminos de la Licencia Publica General de GNU tal como se publica por la
# Free Software Foundation; ya sea la version 3 de la Licencia, o (a su
# eleccion) cualquier version posterior.
#
# Este programa se distribuye con la esperanza de que le sea util, pero SIN
# NINGUNA GARANTIA; sin incluso la garantia implicita de MERCANTILIDAD o
# IDONEIDAD PARA UN PROPOSITO PARTICULAR.
#
# Vea la Licencia Publica General GNU para mas detalles.
#
# Deberia haber recibido una copia de la Licencia Publica General de GNU
# junto con este programa, si no es asi, escriba a la Free Software Foundation,
# Inc, 59 Temple Place - Suite 330, Boston, MA 02111-1307, EE.UU.
#
##############################################################################
# ARCHIVO             : action.py
# AUTOR               : Norman Ruiz.
# COLABORADORES       : No aplica.
# VERSION             : 1.00 estable.
# FECHA DE CREACION   : 05/05/2022.
# ULTIMA ACTUALIZACION: 04/08/2022.
# LICENCIA            : GPL (General Public License) - Version 3.
#=============================================================================
# SISTEMA OPERATIVO   : Linux NT-9992031 4.4.0-19041-Microsoft
#                       #488-Microsoft Mon Sep 01 13:43:00 PST 2020 x86_64 GNU/Linux.
# IDE                 : Atom 1.60.0.
# COMPILADOR          : Python 3.9.2.
# LICENCIA            : GPL (General Public License) - Version 3.
#=============================================================================
# DEDICATORIA: A mi hija Micaela Ruiz que me re aguanta.
#=============================================================================
# DESCRIPCION:
#             Este archivo incluye la definicion del modulo action.
#
#             Las funciones target permiten la carga de terminales ya en
#             circuito de migracion para ser excluidas del armado del nuevo
#             lote de terminales a incluir en el proceso.
#
#-------------------------------------------------------------------------------
# ARCHIVO DE CABECERA: No aplica
#
# FUNCIONES DEFINIDAS:
#==============================================================================|
#     NOMBRE     |  TIPO  |                    ACCION                          |
#================+========+====================================================|
# Anexar_lote()  |  bool  | Inserta y/o actualiza el nuevo lote de terminales  |
#                           en el proceso de migracion.                        |
#----------------+--------+----------------------------------------------------|
# Impactar_cambio() |  void  | Ejecuta l Llama a la accion de insert o update  |
#                              en la base de datos.                            |
#================+========+====================================================|
#
#-------------------------------------------------------------------------------
# MODIFICACIONES DE LA VERSION 0.01 estable (05/05/2022)
# AUTOR DE LA MODIFICACION: Norman Ruiz.
# * Ejemplo de historial de modificaciones.
#
#-------------------------------------------------------------------------------
#
#///////////////////////////////////////////////////////////////////////////////

#*****************************************************************************
#                             INCLUSIONES ESTANDAR
#=============================================================================
import files_bot.logger as log
import files_bot.conection as data_conection
from threading import Thread

#*****************************************************************************
#                             INCLUSIONES PARA WINDOWS
#=============================================================================

# Sin especificar

#*****************************************************************************
#                             INCLUSIONES PARA LINUX
#=============================================================================

# Sin especificar

#*****************************************************************************
#               ESPACIO DE NOMBRES DE LA LIBRERIA
#=============================================================================

# Sin especificar

#***************************************************************************
#                        FUNCIONES PARA LINUX
#===========================================================================
# FUNCION   : bool Anexar_lote(dict, dict).
# ACCION    : Inserta y/o actualiza el nuevo lote de terminales en el proceso de migracion.
# PARAMETROS: dict, parametros de configuracion del bot.
#             dict, el lote de terminales a procesar.
# DEVUELVE  : bool, True si el subproceso finalizo sin errores,
#             o False en caso contrario
#---------------------------------------------------------------------------
def Anexar_lote(parametros, nuevo_lote):
    status = True
    count_i = 0
    count_u = 0
    ubicacion = "data_destiny"
    nonquery_i = parametros["data_conection"][ubicacion]["nonquery_i"]
    nonquery_u = parametros["data_conection"][ubicacion]["nonquery_u"]
    cursor = None
    threads = []
    thread = 0
    count = 0
    max_threads = parametros["max_multithread"]
    threadsregistros = {}


    try:
        mensaje = "Aplicando los cambios del nuevo lote..."
        print(" ", mensaje)
        mensaje = "Ejecunatdo nonquerys contra " + ubicacion + "..."
        log.Escribir_log(mensaje)
        mensaje = "Nonquery insert: " + nonquery_i
        log.Escribir_log(mensaje)
        mensaje = "Nonquery update: " + nonquery_u
        log.Escribir_log(mensaje)

        mensaje = "Comenzando escritura de datos..."
        log.Escribir_log(mensaje)

        registros = len(nuevo_lote)

        if (registros % max_threads != 0):
            registros += max_threads

        registros_threds = registros // max_threads

        for terminal, accion in nuevo_lote.items():
            threadsregistros[terminal] = list(accion)
            count += 1
            if (count == registros_threds):
                conexion = data_conection.Conectar(parametros, ubicacion)
                threads.append(Thread(target=Impactar_cambio, args=(conexion, ubicacion, nonquery_i, nonquery_u, dict(threadsregistros))))
                count = 0
                threadsregistros.clear()

        conexion = data_conection.Conectar(parametros, ubicacion)
        threads.append(Thread(target=Impactar_cambio, args=(conexion, ubicacion, nonquery_i, nonquery_u, dict(threadsregistros))))
        count = 0
        threadsregistros.clear()

        for thread in threads:
        	thread.start()

        for thread in threads:
        	thread.join()

        mensaje = "Escritura de datos finalizada..."
        log.Escribir_log(mensaje)
        mensaje = "Subproceso finalizado..."
        print(" ", mensaje)
        log.Escribir_log(mensaje)
    except Exception as excepcion:
        status = False
        mensaje = "Error - Carga de configuracion: " + excepcion
        log.Escribir_log(mensaje)
        print(" ", mensaje)
    finally:
        if not(status):
            mensaje = "WARNING!!! - Subproceso interrumpido..."
            print(" ", mensaje)
            log.Escribir_log("--------------------------------------------------------------------------------")
            log.Escribir_log(mensaje)

        return status

#---------------------------------------------------------------------------
# FUNCION   : void Impactar_cambio(objeto_conexion, string, string, string, dict)
# ACCION    : Inserta y/o actualiza el nuevo lote de terminales en el proceso de migracion.
# PARAMETROS: objeto_conexion, la conecion contra la base de datos
#             string, la ubicacion  a la que apunta la conexion
#             string, la nonquery para los insert
#             string, la nonquery para los update
#             dict, el lote de terminales a impactar
# DEVUELVE  : void, no devuelve nada.
#---------------------------------------------------------------------------
def Impactar_cambio(conexion, ubicacion, nonquery_i, nonquery_u, nuevo_lote):
        cursor = conexion.cursor()
        for terminal, accion in nuevo_lote.items():
            if accion[0] == 'i':
                data_conection.Insertar_nuevos(conexion, cursor, nonquery_i, terminal, accion[1])
            else:
                data_conection.Actualizar_existentes(conexion, cursor, nonquery_u, terminal, accion[1])
        cursor.close()
        data_conection.Desconectar(conexion, ubicacion)


#***************************************************************************
#                        FUNCIONES PARA WINDOWS
#===========================================================================
# FUNCION   :
# ACCION    :
# PARAMETROS:
# DEVUELVE  :
#---------------------------------------------------------------------------

# Sin especificar

#=============================================================================
#                            FIN DE ARCHIVO
##############################################################################
