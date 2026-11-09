"""Contenido de las páginas de tratamiento (/tratamientos/<slug>).

Texto informativo para pacientes: describe la enfermedad y el enfoque general, sin prometer
resultados. Cualquier cambio médico debe revisarlo el Dr. Gavilanes antes de publicarse.
Después de editar, ejecutar:  python scripts/generar_tratamientos.py
"""

WA = 'https://wa.me/593998340502?text='

TRATAMIENTOS = [
    {
        'slug': 'varices-endolaser',
        'nombre': 'Várices con endoláser',
        'titulo': 'Várices con endoláser en Quito y Cumbayá | Dr. Gavilanes',
        'descripcion': 'Tratamiento de várices con endoláser en Quito y Cumbayá: sin cirugía abierta, guiado por Eco Doppler. Valoración con el Dr. Patricio Gavilanes.',
        'h1': 'Tratamiento de várices con endoláser en Quito y Cumbayá',
        'intro': 'Las várices son venas dilatadas y tortuosas, casi siempre en las piernas, que aparecen cuando las válvulas de las venas dejan de cerrar bien y la sangre se acumula. El endoláser permite cerrar la vena enferma desde su interior, sin cirugía abierta.',
        'tipo': 'MedicalProcedure',
        'condicion': 'Insuficiencia venosa crónica (várices)',
        'icono': 'i-zap',
        'secciones': [
            ('¿Por qué aparecen las várices?', [
                'Influyen la herencia, los embarazos, pasar muchas horas de pie o sentado, el sobrepeso y la edad. Con el tiempo, la presión en la vena aumenta y se vuelve visible y abultada.',
                'No son solo un tema estético: sin control pueden causar hinchazón, manchas en la piel, flebitis y, en casos avanzados, úlceras cerca de los tobillos.',
            ]),
            ('¿En qué consiste el endoláser?', [
                'Con anestesia local y guía de ecografía, se introduce una fibra láser muy fina en la vena enferma a través de una pequeña punción. La energía del láser cierra la vena desde adentro y la sangre pasa a circular por venas sanas.',
                'En la mayoría de los casos el paciente camina el mismo día y retoma sus actividades en pocos días, con medias de compresión durante el tiempo que indique el doctor.',
            ]),
            ('¿Soy candidato?', [
                'No todas las várices se tratan igual. La decisión se toma después de la consulta y de un Eco Doppler, que muestra qué venas están afectadas y cómo circula la sangre. Según el caso, el endoláser puede combinarse con escleroterapia u otras técnicas.',
            ]),
        ],
        'sintomas': ['Piernas pesadas o cansadas', 'Hinchazón al final del día', 'Venas abultadas', 'Calambres nocturnos', 'Picazón o ardor', 'Manchas oscuras en los tobillos'],
        'preguntas': [
            ('¿El endoláser duele?', 'Se realiza con anestesia local. Durante el procedimiento se siente presión o leves molestias; después puede haber sensibilidad o pequeños moretones que ceden en días.'),
            ('¿Las várices pueden volver a salir?', 'La vena tratada queda cerrada, pero la tendencia a formar várices puede continuar en otras venas. Por eso se recomiendan controles y hábitos como caminar, evitar estar mucho tiempo inmóvil y usar compresión cuando se indique.'),
        ],
        'wa': 'Hola Dr. Gavilanes, quisiera información sobre el tratamiento de várices con endoláser.',
    },
    {
        'slug': 'aranas-vasculares',
        'nombre': 'Arañas vasculares',
        'titulo': 'Arañas vasculares y escleroterapia en Quito | Dr. Gavilanes',
        'descripcion': 'Escleroterapia para arañas vasculares y venas pequeñas en Quito y Cumbayá. Valoración previa con el cirujano vascular Dr. Patricio Gavilanes.',
        'h1': 'Arañas vasculares: escleroterapia en Quito y Cumbayá',
        'intro': 'Las arañas vasculares (telangiectasias) son venitas finas, rojas o violáceas, que se ven bajo la piel de las piernas. Suelen ser una molestia estética, aunque a veces causan ardor o cansancio y pueden acompañar a una insuficiencia venosa más profunda.',
        'tipo': 'MedicalProcedure',
        'condicion': 'Telangiectasias (arañas vasculares)',
        'icono': 'i-drop',
        'secciones': [
            ('¿Qué es la escleroterapia?', [
                'Es la aplicación, con agujas muy finas, de un medicamento que irrita la pared de la vena pequeña y hace que se cierre. Con las semanas, el cuerpo la reabsorbe y deja de verse.',
                'Suelen necesitarse varias sesiones, separadas por algunas semanas, según la cantidad y el tamaño de las venas.',
            ]),
            ('Antes de tratar, revisar las venas profundas', [
                'Si las arañas se deben a una vena más grande que no funciona bien, tratar solo la superficie da resultados cortos. Por eso, cuando hace falta, el doctor indica un Eco Doppler antes de la escleroterapia.',
            ]),
            ('Después de cada sesión', [
                'Se puede caminar enseguida y volver a la rutina. Durante unos días se recomiendan medias de compresión y evitar el sol directo y el ejercicio intenso, según las indicaciones que reciba en consulta.',
            ]),
        ],
        'sintomas': ['Venitas rojas o violáceas', 'Ardor o picazón', 'Piernas cansadas', 'Aparecen con el embarazo o con los años'],
        'preguntas': [
            ('¿Cuántas sesiones necesito?', 'Depende de cada caso. En la valoración el doctor le explica cuántas sesiones estima y qué resultado esperar.'),
            ('¿Pueden salir nuevas arañas?', 'Sí, la tendencia puede continuar con el tiempo. Las sesiones de mantenimiento y los cuidados diarios ayudan a controlarlas.'),
        ],
        'wa': 'Hola Dr. Gavilanes, quisiera información sobre el tratamiento de arañas vasculares.',
    },
    {
        'slug': 'pie-diabetico',
        'nombre': 'Pie diabético',
        'titulo': 'Pie diabético en Quito y Cumbayá | Dr. Patricio Gavilanes',
        'descripcion': 'Prevención y tratamiento del pie diabético en Quito y Cumbayá: úlceras, heridas que no cicatrizan y mala circulación. Valoración vascular a tiempo.',
        'h1': 'Pie diabético: prevención y tratamiento en Quito y Cumbayá',
        'intro': 'El pie diabético son las lesiones del pie causadas por la diabetes, por daño en los nervios (menos sensibilidad) y en la circulación. Una herida pequeña puede complicarse rápido, por eso la valoración vascular temprana es clave.',
        'tipo': 'MedicalTherapy',
        'condicion': 'Pie diabético',
        'icono': 'i-foot',
        'secciones': [
            ('¿Por qué la circulación importa tanto?', [
                'Para que una herida cicatrice necesita sangre que llegue con oxígeno. Cuando las arterias de la pierna están estrechas, las úlceras tardan mucho en sanar o se infectan.',
                'El cirujano vascular evalúa la circulación con examen físico y Eco Doppler y, si hace falta, propone mejorar el flujo con técnicas endovasculares.',
            ]),
            ('Manejo integral', [
                'El tratamiento combina curación de las heridas, control de la infección, descarga del pie (evitar apoyar la zona lesionada), control de la glucosa junto con su médico tratante y, cuando corresponde, revascularización.',
                'El objetivo es cerrar la herida y conservar la extremidad.',
            ]),
            ('Prevención en casa', [
                'Revise sus pies todos los días, incluso entre los dedos. Use calzado cómodo y medias sin costuras apretadas, no camine descalzo, corte las uñas rectas y consulte ante cualquier herida, ampolla o cambio de color.',
            ]),
        ],
        'sintomas': ['Heridas que no cicatrizan', 'Pies fríos o pálidos', 'Adormecimiento u hormigueo', 'Cambios de color en la piel', 'Dolor al caminar', 'Callos con manchas oscuras'],
        'preguntas': [
            ('¿Cuándo debo consultar?', 'Ante cualquier herida que no mejore en pocos días, enrojecimiento, secreción, mal olor o un pie más frío o pálido que el otro. Si hay fiebre o el pie cambia de color de forma brusca, acuda a emergencias.'),
            ('¿Tengo que dejar a mi médico de la diabetes?', 'No. El manejo vascular se coordina con su médico tratante, que sigue a cargo del control de la diabetes.'),
        ],
        'wa': 'Hola Dr. Gavilanes, quisiera una valoración por pie diabético.',
    },
    {
        'slug': 'trombosis-venosa',
        'nombre': 'Trombosis venosa',
        'titulo': 'Trombosis venosa profunda en Quito | Dr. Patricio Gavilanes',
        'descripcion': 'Diagnóstico con Eco Doppler y tratamiento de la trombosis venosa profunda en Quito y Cumbayá, para prevenir complicaciones como la embolia pulmonar.',
        'h1': 'Trombosis venosa profunda: diagnóstico y tratamiento en Quito',
        'intro': 'La trombosis venosa profunda es la formación de un coágulo dentro de una vena, casi siempre de la pierna. Es una condición que requiere atención oportuna: el coágulo puede desprenderse y llegar al pulmón (embolia pulmonar).',
        'tipo': 'MedicalTherapy',
        'condicion': 'Trombosis venosa profunda',
        'icono': 'i-alert',
        'alerta': 'Acuda a emergencias si presenta falta de aire repentina, dolor en el pecho, tos con sangre o hinchazón y dolor brusco en una sola pierna.',
        'secciones': [
            ('Factores de riesgo', [
                'Inmovilidad prolongada (viajes largos, reposo en cama, cirugías recientes), embarazo y posparto, anticonceptivos u hormonas, cáncer, obesidad, antecedentes familiares de trombosis y algunas alteraciones de la coagulación.',
            ]),
            ('¿Cómo se diagnostica?', [
                'El Eco Doppler venoso es el examen principal: muestra si hay un coágulo, dónde está y su extensión, sin dolor ni radiación. Se complementa con la valoración clínica y, cuando hace falta, exámenes de sangre.',
            ]),
            ('Tratamiento y seguimiento', [
                'La base del tratamiento son los anticoagulantes, que evitan que el coágulo crezca y ayudan al cuerpo a disolverlo. En casos seleccionados se consideran técnicas endovasculares.',
                'El seguimiento busca prevenir nuevos episodios y el síndrome postrombótico (hinchazón y molestias crónicas en la pierna).',
            ]),
        ],
        'sintomas': ['Hinchazón en una sola pierna', 'Dolor o tensión en la pantorrilla', 'Piel caliente o enrojecida', 'Venas superficiales más visibles'],
        'preguntas': [
            ('¿Cuánto tiempo dura el tratamiento?', 'Depende de la causa y del riesgo de cada paciente; suele ser de varios meses. El doctor define la duración y los controles en consulta.'),
            ('¿Puedo prevenir una trombosis en un viaje largo?', 'Muévase y camine cada cierto tiempo, mueva los tobillos cuando esté sentado e hidrátese. Si tiene factores de riesgo, consulte antes del viaje: puede necesitar medias de compresión u otras medidas.'),
        ],
        'wa': 'Hola Dr. Gavilanes, quisiera una valoración por trombosis venosa.',
    },
    {
        'slug': 'enfermedad-arterial',
        'nombre': 'Enfermedad arterial',
        'titulo': 'Mala circulación arterial en Quito | Dr. Patricio Gavilanes',
        'descripcion': 'Enfermedad arterial periférica en Quito y Cumbayá: dolor al caminar, pies fríos y heridas. Diagnóstico con Eco Doppler y tratamiento endovascular.',
        'h1': 'Enfermedad arterial periférica: mala circulación en las piernas',
        'intro': 'La enfermedad arterial periférica es el estrechamiento de las arterias de las piernas, casi siempre por aterosclerosis (placas de colesterol). La sangre llega con dificultad a los músculos y a la piel.',
        'tipo': 'MedicalProcedure',
        'condicion': 'Enfermedad arterial periférica',
        'icono': 'i-activity',
        'alerta': 'Acuda a emergencias si un pie o una pierna se vuelve de repente frío, pálido, muy doloroso o pierde fuerza.',
        'secciones': [
            ('Señal típica: dolor al caminar', [
                'Muchos pacientes sienten dolor o calambre en la pantorrilla al caminar cierta distancia, que se alivia al detenerse (claudicación). En etapas avanzadas hay dolor en reposo, sobre todo de noche, y heridas que no cicatrizan.',
                'Es más frecuente en personas que fuman, con diabetes, hipertensión, colesterol alto o mayores de 60 años.',
            ]),
            ('Diagnóstico', [
                'Se evalúan los pulsos y la presión en tobillos y brazos, y el Eco Doppler arterial muestra dónde están las obstrucciones y cuánto afectan el flujo.',
            ]),
            ('Opciones de tratamiento', [
                'El primer paso es controlar los factores de riesgo: dejar de fumar, caminar con un plan de ejercicio y tratar la diabetes, la presión y el colesterol. Según el caso se indican medicamentos.',
                'Cuando la obstrucción limita la vida diaria o pone en riesgo la pierna, puede abrirse la arteria desde adentro con angioplastia o stent, a través de una pequeña punción, o con cirugía de bypass.',
            ]),
        ],
        'sintomas': ['Dolor en la pantorrilla al caminar', 'Pies fríos', 'Piel pálida o brillante', 'Menos vello en las piernas', 'Heridas que no cicatrizan', 'Dolor nocturno en el pie'],
        'preguntas': [
            ('¿La mala circulación tiene cura?', 'Es una enfermedad crónica, pero con control de los factores de riesgo y el tratamiento adecuado se puede mejorar la distancia que camina y proteger la pierna.'),
            ('¿Es lo mismo que las várices?', 'No. Las várices afectan a las venas, que regresan la sangre al corazón; la enfermedad arterial afecta a las arterias, que la llevan hacia las piernas. Los síntomas y el tratamiento son distintos.'),
        ],
        'wa': 'Hola Dr. Gavilanes, quisiera una valoración por mala circulación arterial.',
    },
    {
        'slug': 'malformaciones-vasculares',
        'nombre': 'Malformaciones vasculares',
        'titulo': 'Malformaciones vasculares en Quito | Dr. Patricio Gavilanes',
        'descripcion': 'Diagnóstico y tratamiento de malformaciones vasculares en niños y adultos en Quito y Cumbayá, con técnicas mínimamente invasivas.',
        'h1': 'Malformaciones vasculares en niños y adultos',
        'intro': 'Las malformaciones vasculares son alteraciones en la formación de venas, arterias o vasos linfáticos presentes desde el nacimiento, aunque a veces se notan años después. Pueden verse como manchas, bultos o zonas de color azulado en la piel.',
        'tipo': 'MedicalProcedure',
        'condicion': 'Malformaciones vasculares',
        'icono': 'i-users',
        'secciones': [
            ('Tipos más frecuentes', [
                'Se clasifican según el vaso afectado: venosas, linfáticas, capilares, arteriovenosas o mixtas. Cada tipo tiene un comportamiento y un tratamiento distinto, por eso el diagnóstico preciso es el primer paso.',
            ]),
            ('¿Cómo se estudian?', [
                'La valoración incluye examen clínico y Eco Doppler; en algunos casos se complementa con resonancia u otros estudios de imagen para conocer su extensión.',
            ]),
            ('Tratamiento', [
                'Muchas malformaciones solo requieren control. Cuando causan dolor, crecen, sangran o afectan la función, existen tratamientos mínimamente invasivos como la escleroterapia guiada por imagen o la embolización, y en casos seleccionados cirugía.',
                'En niños, el plan se decide junto con la familia y, cuando hace falta, con otros especialistas.',
            ]),
        ],
        'sintomas': ['Mancha o bulto azulado', 'Aumento de tamaño con el esfuerzo', 'Dolor o sensación de peso', 'Diferencia de tamaño entre extremidades'],
        'preguntas': [
            ('¿Una malformación vascular es un tumor?', 'No. Es una alteración en la formación de los vasos, no un cáncer. Se diferencia de los hemangiomas, que son tumores benignos propios de los bebés.'),
            ('¿Siempre hay que operarla?', 'No. Depende del tipo, el tamaño y los síntomas. Muchas se controlan y otras se tratan con procedimientos por punción.'),
        ],
        'wa': 'Hola Dr. Gavilanes, quisiera información sobre malformaciones vasculares.',
    },
    {
        'slug': 'puerto-subcutaneo',
        'nombre': 'Puerto subcutáneo',
        'titulo': 'Colocación de puerto subcutáneo en Quito | Dr. Gavilanes',
        'descripcion': 'Colocación de puerto subcutáneo (catéter implantable) en Quito y Cumbayá para quimioterapia y tratamientos intravenosos prolongados.',
        'h1': 'Colocación de puerto subcutáneo (catéter implantable)',
        'intro': 'El puerto subcutáneo es un pequeño dispositivo que se coloca bajo la piel, generalmente debajo de la clavícula, conectado a un catéter que llega a una vena grande. Permite recibir quimioterapia, medicamentos o extracciones de sangre sin pinchar las venas del brazo cada vez.',
        'tipo': 'MedicalProcedure',
        'condicion': None,
        'icono': 'i-syringe',
        'secciones': [
            ('¿Quién lo necesita?', [
                'Pacientes que reciben quimioterapia, antibióticos o nutrición por vena durante semanas o meses, o que tienen venas difíciles de canalizar. La indicación la coordina su médico tratante (por ejemplo, el oncólogo).',
            ]),
            ('El procedimiento', [
                'Se realiza en quirófano, con anestesia local y sedación según el caso, guiado por ecografía y radioscopia. Deja una pequeña cicatriz y, por lo general, el paciente regresa a casa el mismo día.',
            ]),
            ('Cuidados', [
                'Mientras no se use, el puerto se lava periódicamente con solución según el protocolo de su centro de tratamiento. Consulte de inmediato si nota fiebre, enrojecimiento, dolor o hinchazón en la zona o en el brazo.',
                'Cuando el tratamiento termina, el puerto se retira con un procedimiento corto.',
            ]),
        ],
        'sintomas': [],
        'preguntas': [
            ('¿Se nota bajo la ropa?', 'Se percibe un pequeño relieve bajo la piel, pero no queda nada expuesto: puede bañarse y vestirse con normalidad una vez cicatrizada la herida.'),
            ('¿Duele cuando lo usan?', 'Se accede con una aguja especial a través de la piel; la molestia es similar a la de un pinchazo y puede aliviarse con anestesia en crema.'),
        ],
        'wa': 'Hola Dr. Gavilanes, quisiera información sobre la colocación de un puerto subcutáneo.',
    },
    {
        'slug': 'eco-doppler-vascular',
        'nombre': 'Eco Doppler vascular',
        'titulo': 'Eco Doppler vascular en Quito y Cumbayá | Dr. Gavilanes',
        'descripcion': 'Eco Doppler venoso y arterial en Quito y Cumbayá: muestra el flujo de la sangre sin dolor ni radiación. Base del diagnóstico vascular.',
        'h1': 'Eco Doppler vascular en Quito y Cumbayá',
        'intro': 'El Eco Doppler es una ecografía que, además de la imagen de las venas y arterias, muestra cómo circula la sangre por dentro: su dirección y su velocidad. Es la base del diagnóstico vascular y no causa dolor ni usa radiación.',
        'tipo': 'MedicalTest',
        'condicion': None,
        'icono': 'i-monitor',
        'secciones': [
            ('¿Para qué sirve?', [
                'En las venas detecta válvulas que no cierran (origen de las várices) y coágulos (trombosis). En las arterias muestra estrechamientos u obstrucciones que explican el dolor al caminar o las heridas que no sanan.',
                'También permite planificar procedimientos como el endoláser y controlar los resultados después del tratamiento.',
            ]),
            ('¿Cómo es el examen?', [
                'Se aplica gel sobre la piel y se desliza un transductor por la zona a estudiar, de pie o acostado según el examen. Dura entre 20 y 40 minutos y puede retomar sus actividades enseguida.',
            ]),
            ('Preparación', [
                'Para el estudio de piernas no se necesita ayuno. Use ropa cómoda que permita descubrir la zona. Si va a estudiar arterias del abdomen, se le indicará una preparación específica.',
            ]),
        ],
        'sintomas': ['Piernas pesadas o hinchadas', 'Venas abultadas', 'Dolor al caminar', 'Sospecha de trombosis', 'Control tras un tratamiento'],
        'preguntas': [
            ('¿El Eco Doppler lo realiza el mismo doctor?', 'Sí. El Dr. Gavilanes realiza e interpreta el estudio dentro de la valoración, lo que permite explicarle el resultado y el plan en la misma consulta.'),
            ('¿Necesito una orden médica?', 'No es indispensable: puede agendar directamente su valoración vascular por WhatsApp.'),
        ],
        'wa': 'Hola Dr. Gavilanes, quisiera agendar un Eco Doppler vascular.',
    },
]
