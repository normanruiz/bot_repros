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
# ARCHIVO             : source.py
# AUTOR               : Norman Ruiz.
# COLABORADORES       : No aplica.
# VERSION             : 1.00 estable.
# FECHA DE CREACION   : 05/05/2022.
# ULTIMA ACTUALIZACION: 03/06/2022.
# LICENCIA            : GPL (General Public License) - Version 3.
#=============================================================================
# SISTEMA OPERATIVO   : Linux NT-9992031 4.4.0-19041-Microsoft
#               #488-Microsoft Mon Sep 01 13:43:00 PST 2020 x86_64 GNU/Linux.
# IDE                 : Atom 1.60.0.
# COMPILADOR          : Python 3.9.2.
# LICENCIA            : GPL (General Public License) - Version 3.
#=============================================================================
# DEDICATORIA: A mi hija Micaela Ruiz que me re aguanta.
#=============================================================================
# DESCRIPCION:
#             Este archivo incluye la definicion del modulo source.
#
#             Las funciones source permiten la recoleccion de termnales
#             candidatas a ser incorporadas al procesod e migracion por
#             presentar repros pendientes.
#
#-------------------------------------------------------------------------------
# ARCHIVO DE CABECERA: No aplica
#
# FUNCIONES DEFINIDAS:
#==============================================================================|
#     NOMBRE     |  TIPO  |                    ACCION                          |
#================+========+====================================================|
#  Buscar_candidatas() |  dict  | Busca terminales con repros pendientes y     |
#                    las retorna junto al codigo de repro en un diccionario.   |
#----------------+--------+----------------------------------------------------|
#  Contar_repros()  |  int  | Cuenta la cantidad de reprogamaciones dentro del |
#        arreglo independientemente de la termianl a la que pertenesca.        |
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
# FUNCION   : int Contar_repros(dict)
# ACCION    : Cuenta la cantidad de reprogamaciones dentro del arreglo
#             independientemente de la termianl a la que pertenesca.
# PARAMETROS: dict, diccionario con las terminales y sus respectivas
#             reprogramaciones pendientes.
# DEVUELVE  : int, un entero con el recuento de reprogramaciones del
#             diccionario.
#---------------------------------------------------------------------------
def Contar_repros(terminales_candidatas):
    count = 0
    try:
        for terminal, repros in terminales_candidatas.items():
            count += len(repros)
    except Exception as excepcion:
        mensaje = "ERROR - Contabilizando reprogramaciones: " + str(excepcion)
        print(" ", mensaje)
        log.Escribir_log(mensaje)
    finally:
        return count

#---------------------------------------------------------------------------
# FUNCION   : dict Buscar_candidatas(dict).
# ACCION    : Busca terminales con repros pendientes y las retorna junto
#             al codigo de repro en un diccionario.
# PARAMETROS: dict, parametros de configuracion del bot.
# DEVUELVE  : dict, coleccion con las terminales y sus repros.
#---------------------------------------------------------------------------
def Buscar_candidatas(parametros):
    ubicacion ="data_source"
    terminales_candidatas = {}
    consulta = parametros["data_conection"][ubicacion]["query"]
    conexion = None
    status = True
    try:
        mensaje = "Buscando terminales candidatas..."
        print(" ", mensaje)
        log.Escribir_log(mensaje)
        conexion = data_conection.Conectar(parametros, ubicacion)
        if conexion:
            terminales_candidatas = data_conection.Ejecutar_consulta_origen(conexion, ubicacion, consulta)
            mensaje = "Terminales detectadas: " + str(len(terminales_candidatas.keys()))
            print(" ", mensaje)
            log.Escribir_log(mensaje)
            mensaje = "Repros pendientes detectadas: " + str(Contar_repros(terminales_candidatas))
            print(" ", mensaje)
            log.Escribir_log(mensaje)
            mensaje = "Subproceso finalizado..."
            print(" ", mensaje)
            log.Escribir_log(mensaje)
        else:
            status = False
    except Exception as excepcion:
        terminales_candidatas = "fallido"
        status = False
        mensaje = "ERROR - Carga de terminales candidatas: " + str(excepcion)
        print(" ", mensaje)
        log.Escribir_log(mensaje)
    finally:
        if not(status):
            mensaje = "WARNING!!! - Subproceso interrumpido..."
            print(" ", mensaje)
            log.Escribir_log(mensaje)
        if conexion:
            data_conection.Desconectar(conexion, ubicacion)
        print()
        log.Escribir_log("--------------------------------------------------------------------------------")
        return terminales_candidatas

#---------------------------------------------------------------------------
# FUNCION   :
# ACCION    :
# PARAMETROS:
# DEVUELVE  :
#---------------------------------------------------------------------------

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
