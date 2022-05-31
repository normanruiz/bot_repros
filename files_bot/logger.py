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
# ARCHIVO             : logger.py
# AUTOR               : Norman Ruiz.
# COLABORADORES       : No aplica.
# VERSION             : 1.00 estable.
# FECHA DE CREACION   : 06/55/2022.
# ULTIMA ACTUALIZACION: 11/05/2022.
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
#             Este archivo incluye la definicion del modulo logger.
#
#             Las funciones logger permiten el registro de logs de las
#             actividades del bot.
#
#-------------------------------------------------------------------------------
# ARCHIVO DE CABECERA: No aplica
#
# FUNCIONES DEFINIDAS:
#==============================================================================|
#     NOMBRE     |  TIPO  |                    ACCION                          |
#================+========+====================================================|
# Verificar_archivo() | bool | Verifica si el archivo de log del dia existe y  |
#                             de no ser asi lo genera.                         |
#----------------+--------+----------------------------------------------------|
# Escribir_log   |  bool  | Escrive una linea con un mensaje en el rachivo     |
#                           de logs.                                           |
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
import json
from datetime import date
import time

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
#                        FUNCIONES PARA WINDOWS
#===========================================================================
# FUNCION   :
# ACCION    :
# PARAMETROS:
# DEVUELVE  :
#---------------------------------------------------------------------------

# Sin especificar

#***************************************************************************
#                        FUNCIONES PARA LINUX
#===========================================================================
# FUNCION   : bool verificar_archivo()
# ACCION    : Verifica si el archivo de log del dia existe y
#             de no ser asi lo genera.
# PARAMETROS: void
# DEVUELVE  : bool
#---------------------------------------------------------------------------
def Verificar_archivo():
    try:
        filename = "./files_log/log-" + str(date.today()) + ".txt"
        file_log = open(filename, 'r')
    except Exception as excepcion:
        file_log = open(filename, 'w')
        #print("  Error - Escribiendo log:", excepcion)
    finally:
        file_log.close()

#---------------------------------------------------------------------------
# FUNCION   : bool Escribir_log(string).
# ACCION    : Escrive una linea con un mensaje en el rachivo de logs.
# PARAMETROS: string.
# DEVUELVE  : bool
#---------------------------------------------------------------------------
def Escribir_log(texto):
    try:
        Verificar_archivo()
        filename = "./files_log/log-" + str(date.today()) + ".txt"
        file_log = open(filename, 'a')
        mensaje = time.strftime('%H:%M:%S', time.localtime()) + " " + texto + "\n"
        file_log.write(mensaje)
    except Exception as excepcion:
        print("  Error - Escribiendo log:", excepcion)
    finally:
        file_log.close()

#---------------------------------------------------------------------------
# FUNCION   :
# ACCION    :
# PARAMETROS:
# DEVUELVE  :
#---------------------------------------------------------------------------

#=============================================================================
#                            FIN DE ARCHIVO
##############################################################################
