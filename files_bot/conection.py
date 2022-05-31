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
# ARCHIVO             : conection.py
# AUTOR               : Norman Ruiz.
# COLABORADORES       : No aplica.
# VERSION             : 1.00 estable.
# FECHA DE CREACION   : 11/55/2022.
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
#             Este archivo incluye la definicion del modulo conection.
#
#             Las funciones conection permiten la iteraccion con la
#             base de datos.
#
#-------------------------------------------------------------------------------
# ARCHIVO DE CABECERA: No aplica
#
# FUNCIONES DEFINIDAS:
#==============================================================================|
#     NOMBRE     |  TIPO  |                    ACCION                          |
#================+========+====================================================|
# Buscar_candidatas() | dictionary | Busca terminales con repros pendientes y  |
#                    las retorna junto al codigo de repro en un diccionario.   |
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
import pyodbc

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
# FUNCION   :
# ACCION    :
# PARAMETROS:
# DEVUELVE  :
#---------------------------------------------------------------------------



#---------------------------------------------------------------------------
# FUNCION   : objeto Conectar(dictionary).
# ACCION    : Abre la coneccion contra la base de datos.
# PARAMETROS: dictionary.
# DEVUELVE  : objeto.
#---------------------------------------------------------------------------
def Conectar(parametros, ubicacion):
    conexion = False
    try:
        cadena_de_conexion = 'DRIVER=' + parametros["data_conection"][ubicacion]["driver"] + ';SERVER=' + parametros["data_conection"][ubicacion]["server"] + ';DATABASE=' + parametros["data_conection"][ubicacion]["database"] + ';UID=' + parametros["data_conection"][ubicacion]["username"] + ';PWD=' + parametros["data_conection"][ubicacion]["password"] + ';TrustServerCertificate=yes'
        conexion = pyodbc.connect(cadena_de_conexion)
    except Exception as excepcion:
        print("  Error - Conectando a base de datos:", excepcion)
    finally:
        return conexion

#---------------------------------------------------------------------------
# FUNCION   :
# ACCION    :
# PARAMETROS:
# DEVUELVE  :
#---------------------------------------------------------------------------
def Desconectar(conexion):
    status = False
    try:
        conexion.close()
        status = True
    except Exception as excepcion:
        print("  Error - Cerrando conexion a base de datos:", excepcion)
    finally:
        return status

#---------------------------------------------------------------------------
# FUNCION   :
# ACCION    :
# PARAMETROS:
# DEVUELVE  :
#---------------------------------------------------------------------------
def Ejecutar_consulta_origen(conexion, consulta):
    data = {}
    aux_terminal = None
    aux_repro = []
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta)
        registro = cursor.fetchone()
        if registro:
            aux_terminal = str(int(registro[0]))
        while registro:
            if aux_terminal == str(int(registro[0])):
                aux_repro.append(str(registro[1]).replace(' ', ''))
            else:
                data[aux_terminal] = list(aux_repro)
                aux_terminal = str(int(registro[0]))
                aux_repro.clear()
                aux_repro.append(str(registro[1]).replace(' ', ''))
            registro = cursor.fetchone()
        data[aux_terminal] = list(aux_repro)
    except Exception as excepcion:
        print("  Error - Ejecutando consulta:", excepcion)
    finally:
        return data

#---------------------------------------------------------------------------
# FUNCION   :
# ACCION    :
# PARAMETROS:
# DEVUELVE  :
#---------------------------------------------------------------------------
def Ejecutar_consulta_destino(conexion, consulta):
    data = {}

    try:
        cursor = conexion.cursor()
        cursor.execute(consulta)
        registro = cursor.fetchone()
        while registro:
            data[registro.terminal] = registro.cant_solicitudes
            registro = cursor.fetchone()
    except Exception as excepcion:
        print("  Error - Ejecutando consulta:", excepcion)
    finally:
        return data


#---------------------------------------------------------------------------
# FUNCION   :
# ACCION    :
# PARAMETROS:
# DEVUELVE  :
#---------------------------------------------------------------------------
def Insertar_nuevos(conexion, nonquery_i, terminal, prioridad):
    status = 0
    try:
        cursor = conexion.cursor()
        count = cursor.execute(nonquery_i, terminal, prioridad).rowcount
        conexion.commit()
        if count == 1:
            status = 1
    except Exception as excepcion:
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
def Actualizar_existentes(conexion, nonquery_u, terminal, solicitudes):
    status = 0
    try:
        cursor = conexion.cursor()
        count = cursor.execute(nonquery_u, solicitudes, terminal).rowcount
        conexion.commit()
        if count == 1:
            status = 1
    except Exception as excepcion:
        mensaje = "Error - Carga de configuracion: " + excepcion
        log.Escribir_log(mensaje)
        print(" ", mensaje)
    finally:
        return status

#=============================================================================
#                            FIN DE ARCHIVO
##############################################################################



# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port


#cursor.execute("SELECT @@version;")
#row = cursor.fetchone()
#while row:
#    print(row[0])
#    row = cursor.fetchone()
