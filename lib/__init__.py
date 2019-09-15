from collections import defaultdict
from utils import config
import glog as log

log.debug('***** Reinitializing ranking models ******')

# map of model name -> word2vec model
# eg title -> word2vec model for titles
models = {}
# names of bin file in s3://vs-models-prod/w2v_exp/, e.g. ['title-ngram-exp-refreshed', 'work-ngram-exp-refreshed', 'skill-ngram-exp-refreshed']
whitelist_w2v_exp_models = {'title-ngram': '', 'work-ngram': '', 'skill': '', 'location-ngram':''}
whitelist_w2v_exp_cnts = {
        'school': '',
        'skill': '',
        'skill_stemmed': '',
        'work': '',
        'work_categories': '',
        'title': '',
        'conference': '',
        'location': '',
    }
# nicknames
nicknames = {}
# map of attribute to map of term to counts
cnt_stats = {}
# percentile for the attribute cnts; map from attribute to dict of percentile:value
percentile_buckets = [10, 20, 30, 40, 50, 60, 70, 80, 90, 95]
cnt_percentiles = {}

rank_stats = {'conference': {}, 'work': {}, 'school': {}}
category_to_school = defaultdict(list)

# map of company name to json metadata for company
company_metadata = {}

# map of entity_name -> canonical_name
entity_syns = {}
# reverse map of above
reverse_entity_syns = {}

# map of major to canonical major w/ inverse index
canonical_majors = {}
canonical_majors_inverse_index = defaultdict(list)

# map of degree to canonical degree w/ inverse index
canonical_degrees = {}
canonical_degrees_inverse_index = defaultdict(list)

title_syns = {
    'manager_sales': 'sales_manager',
    'director_marketing': 'marketing_director',
    'manager_marketing': 'marketing_manager',
    'manager_operations': 'operations_manager',
    'operations_director': 'director_of_operations',
    'manager_business_development': 'business_development_manager',
    'business_development_director': 'director_of_business_development',
    'software_engineer_in_test': 'software_test_engineer',
    'director_sales': 'sales_director',
    'director_of_finance': 'finance_director',
    'director_of_sales': 'sales_director',
    'director_of_marketing': 'marketing_director'
}

# map of attribute name -> [map term -> cluster_id]
# eg title-class50 (cluster titles into 50 categories)
attribute_clusters = {}
cluster_to_model_name = {}
model_to_cluster_names = defaultdict(list)

# map of work:title_class to top skills
skills_by_work_title_class = {}

# map of skill -> CompanySchoolForSkill
company_school_by_skill = {}

# entity/term -> list of logo urls
term_to_logo_urls = {}

# name -> (ethnicity, count) dict
name_to_ethnicity_dict = {}

# idf map
skill_idf = {}

# company scores
company_scores = {}

# tensorflow models
tensorflow_models = {}

sent_tagger = None

# decision tree models
bdt_models = {}

# combination regression models
regression_models = {}

ethnicity_model = None

models_initialized = False

translations = {}
region_langs = config.get_region_langs()

def set_model_initialized(val=True):
    global models_initialized
    models_initialized = val


def is_model_initialized():
    global models_initialized
    return models_initialized
