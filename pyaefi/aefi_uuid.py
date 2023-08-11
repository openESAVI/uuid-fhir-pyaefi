# -*- coding: utf-8 -*-

import uuid

class AefiUUID:
    '''
    AefiUUID class generates a UUID version 5 for the AEFI report based on the FHIR QuestionnaireResponse resource.
    '''

    __uuid_v5_url_namespace: str = 'https://paho.org/esavi'
    __country_code: str = None

    def __init__(self, country_code: str):
        self.__country_code = country_code
    
    def generate_aefi_id(self, seed: str) -> uuid.uuid5:
        '''
        Generates a UUID version 5 for the AEFI report based on the FHIR QuestionnaireResponse resource.
        '''
        return uuid.uuid5(uuid.NAMESPACE_URL, '{0}/{1}/{2}'.format(
            self.__uuid_v5_url_namespace, 
            self.__country_code, 
            seed
        ))
    
    def generate_aefi_patient_id(self, seed: str) -> uuid.uuid5:
        '''
        Generates a UUID version 5 for the AEFI patient based on the FHIR QuestionnaireResponse resource.
        '''
        return uuid.uuid5(uuid.NAMESPACE_URL, '{0}/{1}/{2}/{3}'.format(
            self.__uuid_v5_url_namespace, 
            self.__country_code, 
            'patient',
            seed
        ))
    