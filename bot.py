##############################################################################
# ARCHIVO             : bot.py
# AUTOR/ES            : Ruiz Norman
# VERSION             : 0.01 beta.
# FECHA DE CREACION   : 03/05/2022.
# ULTIMA ACTUALIZACION: 09/05/2022.
# LICENCIA            : GPL (General Public License) - Version 3.
#  **************************************************************************
#  * El software libre no es una cuestion economica sino una cuestion etica *
#  **************************************************************************
#
# Este programa es software libre;  puede redistribuirlo  o  modificarlo bajo
# los terminos de la Licencia Publica General de GNU  tal como se publica por
# la  Free Software Foundation;  ya sea la version 3 de la Licencia,  o (a su
# eleccion) cualquier version posterior.
#
# Este programa se distribuye con la esperanza  de que le sea util,  pero SIN
# NINGUNA  GARANTIA;  sin  incluso  la garantia implicita de MERCANTILIDAD  o
# IDONEIDAD PARA UN PROPOSITO PARTICULAR.
#
# Vea la Licencia Publica General GNU para mas detalles.
#
# Deberia haber recibido una copia de la Licencia Publica General de GNU junto
# con este proyecto, si no es asi, escriba a la Free Software Foundation, Inc,
# 59 Temple Place - Suite 330, Boston, MA 02111-1307, EE.UU.

#=============================================================================
# SISTEMA OPERATIVO   : Linux NT-9992031 4.4.0-19041-Microsoft
#                       #488-Microsoft Mon Sep 01 13:43:00 PST 2020 x86_64 GNU/Linux.
# IDE                 : Atom 1.60.0.
# COMPILADOR          : Python 3.9.2.
# LICENCIA            : GPL (General Public License) - Version 3.
#=============================================================================
# DESCRIPCION:
#              Bot de recoleccion de terminales con repros pendientes.
#
#/////////////////////////////////////////////////////////////////////////////

#*****************************************************************************
#                       CONFIGURACION MULTIPLATAFORMA
#=============================================================================
# COMPILACION EN WINDOWS
#-----------------------------------------------------------------------------
# Si este programa se va a compilar en Windows, descomente las tres lineas
# siguientes, y comente las tres lineas de "COMPILACION EN LINUX".
#-----------------------------------------------------------------------------

# Sin especificar

#=============================================================================
# COMPILACION EN LINUX
#-----------------------------------------------------------------------------
# Si este programa se va a compilar en Linux, descomente las tres lineas
# siguientes, y comente las tres lineas de "COMPILACION EN WINDOWS".
#-----------------------------------------------------------------------------

# Sin especificar

#*****************************************************************************
#                             DECLARACIONES GLOBALES
#=============================================================================

# Sin especificar

#*****************************************************************************
#                             INCLUSIONES ESTANDAR
#=============================================================================
import os

#*****************************************************************************
#                             INCLUSIONES PERSONALES
#=============================================================================
import files_bot.logger as log
import files_bot.config as configuracion
import files_bot.source as origen
import files_bot.target as destino
import files_bot.filter as filtro
import files_bot.action as accion

#==============================================================================
# DECLARACION DEL ESPACIO DE NOMBRES POR DEFECTO
#------------------------------------------------------------------------------

# Sin especificar

#==============================================================================
# FUNCION PRINCIPAL - PUNTO DE INICIO DEL PROYECTO
#------------------------------------------------------------------------------
status_code = 0
try:
    os.system('clear')
    print()
    print(" ================================================================================")
    print("  Iniciando Repro's Bot...")
    print(" ================================================================================")
    print()
    log.Escribir_log("================================================================================")
    log.Escribir_log("Iniciando Repro's Bot...")
    # Cargo la configuracion desde un archivo
    parametros = configuracion.Cargar()
    print()
    # Defino un diccionario terminal/repro con el valor devuelto por la funcion Buscar_candidatas
    terminales_candidatas = origen.Buscar_candidatas(parametros)
    print()
    # Defino una list de terminales con el valor devuelto por la funcion Buscar_terminales_miembro
    terminales_miembro = destino.Buscar_terminales_miembro(parametros)
    print()
    # Defino un diccionario terminal/prioridad con el valor devuelto por la funcion Generar_nuevo_lote
    nuevo_lote = filtro.Generar_nuevo_lote(parametros, terminales_candidatas, terminales_miembro)
    print()
    # Llamo la funcion Anexar_lote para incorporar las nuevas terminales al proceso de migracion
    accion.Anexar_lote(parametros, nuevo_lote)
except Exception as excepcion:
    status_code = 1
    mensaje = "Error - Ejecucion principal: " + excepcion
    log.Escribir_log(mensaje)
    print("  ", mensaje)
finally:
    log.Escribir_log("Finalizando acciones...")
    log.Escribir_log("================================================================================")
    print()
    print(" ================================================================================")
    print("  Finalizando acciones...")
    print(" ================================================================================")
    print()
#=============================================================================
#                            FIN DE ARCHIVO
##############################################################################
