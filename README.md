<div style="text-align: center;">
    <img src="images/Cover Image.webp" style="display: inline-block; width: 1000px; height: 400px; object-fit: contain; background-position: center; background-repeat: no-repeat; background-size: cover;">
</div>

# Quejas de los Usuarios de Servicios Financieros en Estados Unidos

#### Daniel Alejandro Castillo Martín

CoderHouse

Comisión: 32830

Fecha de entrega: 25-07-2023


---

## 1. Abstract

<p style="text-align: justify;">Los servicios financieros han sido históricamente indispensables para el desarrollo de las personas dentro de una economía, sobre todo si esta cuenta con un enfoque capitalista, y cada día son más usuarios los que requieren de este tipo de servicios. Debido a que es un sector bastante delicado, ya que las entidades que lo conforman son las encargadas de custodiar y gestionar el patrimonio de las personas físicas y morales, por lo que todas estas grandes compañías tienen la responsabilidad y obligación de prestar un servicio digno, adecuado y transparente a los usuarios, brindando confiabilidad y seguridad.</p>


<p style="text-align: justify;">Gracias a esto han surgido diversas entidades gubernamentales en todos los países del mundo, las cuales buscan proteger a los usuarios y regular a todas las empresas que ofrecen este tipo de servicios. Una de ellas es la Oficina para la Protección Financiera del Consumidor (CFPB, por sus siglas en inglés), quien tiene la labor de mediar a la población estadounidense y a las empresas que pertenecen al sector financiero que operan dentro de los Estados Unidos de América.</p>


<p style="text-align: justify;">Las quejas e inconformidades por parte de los usuarios de servicios financieros en Estados Unidos ha ido en aumento durante los últimos años, ya cada vez son más las personas que tienen acceso a este tipo de servicios, esto gracias a la digitalización y a la globalización. Una gran parte de la población puede mostrarse vulnerable ante las grandes instituciones que prestan estos servicios, ya que de ellas depende el correcto manejo y la custodia del patrimonio parcial o total de las personas; es por eso que, como se mencionó anteriormente, surgen estas instituciones gubernamentales que buscan regular y vigilar a las grandes empresas para que estas cumplan con su labor y con sus obligaciones.</p>


<p style="text-align: justify;">La CFPB se ha percatado de dicho incremento en las quejas por parte de los usuarios, y es un tema que ha generado bastante inquietud a la institución, por lo que se ha buscado implementar un plan de acción para vigilar y mediar de mejor manera la relación entre los usuarios y las empresas emisoras de estos servicios y productos. Fue así como la CFPB creó una base de datos con todos los registros de las quejas que presentan todos los usuarios dentro del país estadounidense, la cual está compuesta por 18 columnas que describen cada caso en particular. Dentro de estas columnas podemos encontrar diversas variables que describen el hecho, como el producto por el cuál se presentó la queja, la localización geográfica del cliente, la compañía emisora del servicio, la resolución por parte de la compañía, entre otras.</p>


<p style="text-align: justify;">A continuación, se desarrolla un modelo de diagnóstico y predictivo para identificar qué variables influyen en el descontento de los consumidores de servicios financieros en Estados Unidos, luego de haber obtenido una resolución por haber presentado una queja sobre un producto o servicio.</p>

### 1.1 Hipótesis

<p style="text-align: justify;">Es posible predecir si habrá acuerdo o desacuerdo por parte del usuario ante la resolución que la compañía emisora de un producto o servicio financiero dictamina sobre una queja, analizando distintas variables categóricas que describen la naturaleza de la queja, así como algunas características sociodemográficas del usuario y la descripción de la resolución presentada.</p>

### 1.2 Objetivos

- <p style="text-align: justify;">Generar un diagnóstico previo sobre las quejas de los servicios financieros en todos los estados del país norteamericano, buscando obtener insights importantes para la realización del modelo.</p>
- <p style= "text-align: justify;">Utilizar dicho diagnóstico para identificar patrones y buscar relaciones entre las variables que permitan llevar a cabo una óptima selección de las características más relevantes para la implementación de un modelo supervisado de clasificación.</p>
- <p style= "text-align: justify;">Determinar y predecir con este modelo si un cliente estará satisfecho al momento que se presente la resolución de una queja por parte de la compañía.</p>

### 1.3 Alcance

<p style="text-align: justify;">Se busca desarrollar un modelo que permita identificar potenciales casos de disputas por parte de los clientes cuando presentan una queja ante la CFPB, de acuerdo con la descripción de cada caso (variables independientes). La principal audiencia para este proyecto es tanto la misma CFPB, como las empresas que componen el sistema financiero estadounidense, ya que de esta manera y con la implementación de este modelo  podrían utilizar la data generada y los pronósticos del algoritmo que se utilice para poder identificar de mejor manera los puntos débiles o las deficiencias del sistema en general. Por un lado la CFPB tendría un panorama más claro sobre estos casos, y podría mejorar la forma en cómo se protege al consumidor de estos servicios. Ahora a las empresas también les sería de gran utilidad este modelo, ya que podrían tomar acciones para contrarrestar una potencial disputa al momento de recibir una queja, e identificar las áreas de oportunidad o de mejora en los servicios que proporcionan actualmente.</p>

### 1.4 Preguntas de interés

<p style="text-align: justify;">La tarea del científico de datos en este caso se centra en responder las siguientes preguntas generales:</p>

- <p style="text-align: justify;">¿Cuáles son las variables que tienen un mayor impacto en la satisfacción o insatisfacción de un cliente luego de obtener una resolución sobre una queja por parte de la compañía emisora?</p>


- <p style="text-align: justify;">¿Cómo se han comportado las quejas por parte de los usuarios de servicios financieros a lo largo del tiempo? ¿Se observa algún patrón o relación entre el tiempo y la variable target?</p>


- <p style="text-align: justify;">¿Qué compañías, sectores y productos tienden a tener más conflictos o inconvenientes con sus clientes? Una vez se obtengan los resultados, ¿Sería posible detectar áreas de oportunidad que deriven en mejoras que permitan que exista una mayor transparencia, protección, y en consecuencia, una mejor relación entre el consumidor y la institución emisora?</p>


- <p style="text-align: justify;">¿Existe algún patrón que nos permita identificar cuando la resolución de un conflicto entre la empresa y el cliente no será la deseada? Esto con la finalidad de que la CFPB preste mayor atención a estos casos y pueda mediar la situación de mejor manera.</p>


- <p style="text-align: justify;">¿Existen correlaciones significativas entre algunas de las variables independientes y la variable target?</p>


- <p style="text-align: justify;">¿Podría ser la localización geográfica del usuario un factor determinante en el número resoluciones no satisfactorias sobre las quejas?</p>


<p style="text-align: justify;">Luego de explorar el dataset seleccionado, se generarán una serie de preguntas más específicas, con la finalidad de indagar con mayor profundidad en las preguntas ya presentadas y obtener respuestas más detalladas que ayuden a la generación del modelo y al cumplimiento de los objetivos.</p>

# 2. Estructura del proyecto

- **data/**: Contiene los datos brutos y procesados.
- **notebooks/**: Incluye notebooks para adquisición, limpieza, análisis exploratorio, ingeniería de características y modelado.
- **images/**: Imágenes utilizadas en el análisis y visualizaciones.
- **requirements.txt**: Lista de dependencias necesarias.
- **README.md**: Este documento.

### Instalación y Ejecución

1. **Clona el repositorio:**
   ```sh
   git clone <https://github.com/dancmartin11/dancmartin11-US-Financial-Complaints-Classification-Project.git>
   cd <US-Financial-Complaints-Classification-Project>

2. **Crea y activa un entorno virtual:**
   ```sh
   python -m venv env
   .\env\Scripts\activate

3. **Instala las dependencias:**
   ```sh
    pip install -r requirements.txt

4. **Ejecuta los Notebooks:**

   - Abre Jupyter Notebook:
     ```sh
     jupyter notebook
     ```
   - Navega a la carpeta *notebooks* y sigue el siguiente flujo de ejecución:
     1. `2_data_acquisition.ipynb`
     2. `3_data_wrangling.ipynb`
     3. `4_exploratory_data_analysis.ipynb`
     4. `5_feature_engineering.ipynb`
     5. `6_model_and_evaluation.ipynb`

# 3. Resultados y Conclusiones

A continuación, se muetran los resultados obtenidos por cada uno de los tres modelos:

| **Algoritmo / Métricos**     | **Accuracy**     | **Precision Score**     | **Recall Score**     | **F1 Score**     |
|--------------|--------------|--------------|--------------|--------------|
| **Random Forest** | 58% | 57% | 71% | 64% |
| **LightGBM** | 58% | 57% | 73% | 64% |
| **Logistic Regression** | 58% | 58% | 62% | 60% |

<p style="text-align: justify;">Después de una amplia exploración sobre el conjunto de datos, y la implementación de diversos algoritmos para el desarrollo de modelos de clasificación binaria; se pudo llegar a la conclusión de que con las variables que se tienen dentro de este conjunto, no es del todo posible predecir con un óptimo nivel de efectividad si se generará una disputa luego de la resolución de la queja presentada por un usuario de servicios financieros en los 10 estados con mayor afluencia en el mercado. Sin embargo, se generó un modelo bastante interesante, aquel al que se le implementó  el algoritmo de LightGBM, que si bien, no tiene un nivel elevado de accuracy o precisión, tiene un Recall Score bastante aceptable; llegando al 75%. Esto dictamina que el modelo tiene un buen grado de acierto al momento de detectar verdaderos positivos, es decir; casos en los que se genera una disputa por parte del usuario. Este modelo podría ser de gran uso para predecir el output de una variable que, cabe destacar, es el valor con baja proporción en una variable bastante desbalanceada, por lo que podría ser un modelo de detección de valores atípicos y anticiparse ante una situación extraña.

Además, se atribuye la baja precisión a la naturaleza de las variables, y a la falta de variables descriptivas sociodemográficas sobre los usuarios, por lo que se extiende una recomendación a la CFPB de recopilar más datos y características sobre sus usuarios; por supuesto sin vulnerar su privacidad y con la única finalidad de poder diagnosticar de mejor manera la causa raíz de la presencia de quejas, e identificar aquellas en las que el usuario podría verse vulnerable ante las grandes instituciones financieras del país norteamericano.</p>