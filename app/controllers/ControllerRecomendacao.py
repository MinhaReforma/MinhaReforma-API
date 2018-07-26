# importing necessary libraries
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import (TfidfTransformer, CountVectorizer)
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
import nltk
from nltk.corpus import stopwords

from app.Facade import SQLAlchemy, BaseQuery, db, ModelReforma
Reforma = ModelReforma.Reforma

class ControllerRecomendacao():

        # Profissoes
    prof = ["pedreiro", "encanador", "eletricista", "pintor"]

    pedreiro = [
        'gostaria de contratar alguem pra colocar ceramicas na parede da minha casa',
        'Gostaria de alguém que trabalhasse com assentamento de porcelanato',
        'construção de rodapé decorativo em quarto de 50m2',
        'Necessito de alguém para plicação de forro de gesso',
        'preciso que você compre cimento e areia para colocar a cerâmica',
        'Preciso que voce derrube essa parede da minha casa sem danificar a estrutura de sustentação',
        'Construir um novo comodo, erguer um muro e quebrar parede para instalar uma janela',
        'preciso retocar a argamassa do muro da minha casa, alguns tijolos também precisam ser trocados',
        'preciso de pedreiro para construção de poço artesiano',
        'demolir parede e erguer seis colunas',
        'Preciso que você salpique o meu muro antes de rebocar',
        'abrir uma parede do meu quarto, para por uma porta nova',
        'preciso remover o gesso do teto do panheiro para por pvc no legal',
        'preciso de pedreiro para construir uma churrasqueira na minha laje',
        'construa uma cerca de madeira ao redor da minha casa'
    ]
    encanador = [
        'Cozinha está com a pia entupida, vazamento e refluxo. Ralo da pia entupido, torneira com goteira e refluxo no ralo.',
        'Área de serviço apresenta goteiras no teto, agua podre e cheiro ruim.',
        'problemas encanação do banheiro. O banheiro apresenta goteira, vazamento nas paredes gerando um gasto anormal de água.',
        'Chuveiro do banheiro não cai água. Privada com defeito, quero trocar por um novo vaso sanitário.',
        'Torneira da área de serviço está enferrujada, necessito uma troca.',
        'Desejo uma limpeza nos canos da calha de casa e uma manutenção da mesma.',
        'O ralo do chão do banheiro está saindo um cheiro podre, semelhante a esgoto. Gostaria de ter uma manutenção desse local.',
        'Quero uma instalação do encanamento de uma sauna.',
        'Banheiro precisa de instalação. Instalar bidê, pia, chuveiro, torneira, banheira, mictório.',
        'Quero fazer uma piscina no quintal. Necessito de uma instalação completa no sistema do tanque de água.',
        "Quero certificar que a caixa d'agua esteja em perfeitas situações. Verificar se existe a necessidade de concertar algum cano ou fazer uma troca por outro.",
        'Ajuste nos ralos das termas e troca nos canos de todo o parque aquático.',
        'Manutenção no esgoto da minha casa e do meu apartamento.',
        'Necessito de alguém que  troque e instale vaso sanitário de caixa acoplada',
        'Torneira com problema, água está muito fraca, preciso de alguém que arrume isso'
    ]
    eletricista = [
        'Minhas tomadas sao todas padrão antigo, preciso trocar para tomadas de tres pinos e aterrar todas elas',
        'Instalação de ar condicionado split, trazer todo material necessário',
        'Troca e instalação de chuveiro elétrico, alterar fiação do fio terra',
        'a resistência do chuveiro está dando choque, necessito verificar os fios',
        'preciso de eletricista que concerte tomada da minha máquina de lavar',
        'trocar de uma adaptador de tensão 220v da tomada do minha geladeira que é de 110 Volts',
        'Preciso de um eletricista para instalar um painel de lâmpada led',
        'instalar 3 novas lâmpadas de 15w no banheiro',
        'trocar um disjuntor na casa de fusivel',
        'instação de ventilador de teto',
        'preciso de um eletricista para fazer manutenção no aquecedor',
        'trocar a resistência do chuveiro elétrico e instalar um interruptor para ligar ou desligar o mesmo',
        'quadro de energia elétrica queimou, trocar também contador de corrente',
        'instalar a iluminação da piscina com lâmpadas de led',
        'trocar a fiação da varanda, encapar fio exposto'
    ]
    pintor = [
        'Pintura descascando, preciso repintar dois comodos.',
        'Preciso de alguém que pinte portas de armário de madeira',
        'Necessito de alguém especializado em pinturas de sacadas para texturizar ela',
        'pintor que troque meu quarto de tinta acrílica para tinta fosca da cor rosa',
        'pinte essa parede com tinta azul piscina',
        'preciso de uma demão de tinta no saguão',
        'eu preciso que você dê os retoques finais na casa com pincel grosso',
        'preciso um pintor para pintar a sacada da varanda nas cores da empresa',
        'tintura da parede esta mofando, preciso de uma tinta CORAL anti-mofo',
        'alterar a textura de uma parede ',
        'preciso de um pintor para colar novo papel de parede',
        'utilização de porcelanato liquido para pintar novo cômodo',
        'revestir muro',
        'retocar fachada com tinta epóxi',
        'preciso de um pintor especializado em pintar áreas externas'
    ]

    # X -> features, y -> label
    frases = pedreiro + encanador + eletricista + pintor
    temp = 'pedreiro '*15 + 'encanador '*15 + 'eletricista '*15 + 'pintor '*15
    profissoes = temp.split()

    stops = set(stopwords.words("portuguese"))

    text_clf_svm = Pipeline([('vect', CountVectorizer(stop_words=stops)),
                            ('tfidf', TfidfTransformer()),
                            # ('clf', SGDClassifier(loss='log', penalty='l2', alpha=1e-3, max_iter=5, random_state=42))
                            ('clf', SVC(probability=True, kernel='linear',
                             decision_function_shape='ovo')),
                            ])

    # Parametros
    parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
                'tfidf__use_idf': (True, False),
                # 'clf__alpha': (1e-2, 1e-3),
                }

    def recomendaProfissional(self,id_ref, ref_nome, ref_desc):
        STRING_INPUT_USUARIO = ref_nome + ' ' + ref_desc

        gs_clf_svm = GridSearchCV(self.text_clf_svm, self.parameters, n_jobs=-1)
        gs_clf_svm = gs_clf_svm.fit(self.frases, self.profissoes)
        svm_predictions = gs_clf_svm.predict_proba([STRING_INPUT_USUARIO])
        porcentagens = dict(zip(gs_clf_svm.classes_, svm_predictions[0]))

        ordenados = sorted(porcentagens.items(), key=lambda kv: kv[1], reverse=True)

        reforma = Reforma.query.get(id_ref)
        print("Recomendacao: " + str(ordenados))
        if((ordenados[0][1] - ordenados[1][1]) < 0.15):
            reforma.recomendacao = ordenados[0][0]+' '+ordenados[1][0]
            db.session.add(reforma)
            db.session.commit()
            #return {'profissao': ordenados[0][0] +' ' + ordenados[1][0], 'incerteza':True}
        else:
            reforma.recomendacao = ordenados[0][0]
            db.session.add(reforma)
            db.session.commit()
            #return {'profissao': ordenados[0][0], 'incerteza':False}
        

