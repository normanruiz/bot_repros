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
# FECHA DE CREACION   : 05/55/2022.
# ULTIMA ACTUALIZACION: 05/05/2022.
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
# FUNCION   : <valor de retorno> Anexar_lote().
# ACCION    : Inserta el nuevo lote de terminales en el proceso de migracion.
# PARAMETROS: void.
# DEVUELVE  : Un array Terminales
#---------------------------------------------------------------------------
def Anexar_lote(parametros, nuevo_lote):
    status = 0
    count_i = 0
    count_u = 0
    try:
        print("  Aplicando los cambios del nuevo lote...")
        conexion = data_conection.Conectar(parametros, "data_destiny")
        nonquery_i = parametros["data_conection"]["data_destiny"]["nonquery_i"]
        nonquery_u = parametros["data_conection"]["data_destiny"]["nonquery_u"]
        for terminal, accion in nuevo_lote.items():
            if accion[0] == 'i':
                count_i += data_conection.Insertar_nuevos(conexion, nonquery_i, terminal, accion[1])
            else:
                count_u += data_conection.Actualizar_existentes(conexion, nonquery_u, terminal, accion[1])
        print("  Se incorporaron", count_i, "terminales...")
        print("  Se resolicitaron", count_u, "terminales...")
        print("  Subproceso finalizado...")
    except Exception as excepcion:
        status = 1
        mensaje = "Error - Carga de configuracion: " + excepcion
        log.Escribir_log(mensaje)
        print(" ", mensaje)
    finally:
        return status

#---------------------------------------------------------------------------
# FUNCION   :
# ACCION    :
# PARAMETROS:
# DEVUELVE  :
#---------------------------------------------------------------------------


#=============================================================================
#                            FIN DE ARCHIVO
##############################################################################
