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
# ARCHIVO             : filter.py
# AUTOR               : Norman Ruiz.
# COLABORADORES       : No aplica.
# VERSION             : 1.00 estable.
# FECHA DE CREACION   : 05/55/2022.
# ULTIMA ACTUALIZACION: 06/05/2022.
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
#             Este archivo incluye la definicion del modulo filter.
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
# ejemplo()      |  void  | Hace algo para el ejemplo.                         |
#----------------+--------+----------------------------------------------------|
# ejemplo2()     |  bool  | Hace algo para el ejemplo2.                        |
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

# Sin especificar

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
# FUNCION   : int Priorizar(dic, list)
# ACCION    : se encarga de establecer la prioridad sobre una coleccion de
#      repros, basada en los parametros de priorizacion previamente establecidos
#      en el archivo de configuracion.
# PARAMETROS: dic, los parametros de configuracion del sistema,
#      y list, la coleccion de repros pendientes para priorizar la terminal
# DEVUELVE  : int, la prioridad establecida
#---------------------------------------------------------------------------
def Priorizar(parametros, repros):
    prioridad = 3
    try:
        prioridades = parametros["repros_prioridad"]
        for repro in repros:
            if repro in prioridades:
                if prioridades[repro] < prioridad:
                    prioridad = prioridades[repro]
    except Exception as excepcion:
        print("  Error - Generando lote:", excepcion)
    finally:
        return prioridad

#---------------------------------------------------------------------------
# FUNCION   :
# ACCION    :
# PARAMETROS:
# DEVUELVE  :
#---------------------------------------------------------------------------
def Resolicitar(terminal_candidata, terminales_miembro):
    solicitudes = None
    try:
        solicitudes = terminales_miembro[terminal_candidata] + 1
    except Exception as excepcion:
        print("  Error - Generando lote:", excepcion)
    finally:
        return solicitudes
#---------------------------------------------------------------------------
# FUNCION   :
# ACCION    :
# PARAMETROS:
# DEVUELVE  :
#---------------------------------------------------------------------------
def Generar_nuevo_lote(parametros, terminales_candidatas, terminales_miembro):
    nuevo_lote = {}
    try:
        print("  Generando nuevo lote de terminales...")
        for terminal_candidata, repros in terminales_candidatas.items():
            if terminal_candidata in terminales_miembro:
                nuevo_lote[terminal_candidata] = ["u", Resolicitar(terminal_candidata, terminales_miembro)]
            else:
                nuevo_lote[terminal_candidata] = ["i", Priorizar(parametros, repros)]
        print("  Se genero un lote con:", len(nuevo_lote), " terminales...")
        print("  Subproceso finalizado...")
    except Exception as excepcion:
        print("  Error - Generando lote:", excepcion)
    finally:
        return nuevo_lote

#***************************************************************************
#                        FUNCIONES PARA LINUX
#===========================================================================
# FUNCION   : <valor de retorno> Generar_nuevo_lote().
# ACCION    : Cre< un nuevo lote de terminal es candidatas excluyendo las
#             terminales miembro.
# PARAMETROS: void.
# DEVUELVE  : Un array Terminales
#---------------------------------------------------------------------------


#---------------------------------------------------------------------------
# FUNCION   :
# ACCION    :
# PARAMETROS:
# DEVUELVE  :
#---------------------------------------------------------------------------


#=============================================================================
#                            FIN DE ARCHIVO
##############################################################################
