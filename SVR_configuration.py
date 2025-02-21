# -*- coding: utf-8 -*-


################# SVR parameter setting for different cases ##########################

SVR_parameter = dict()

SVR_parameter['2N to 1N'] = dict()
SVR_parameter['2N to 1N']['Electricity'] = {'C': 200, 'epsilon': 1.0}
SVR_parameter['2N to 1N']['Moisture'] = {'C': 1.0, 'epsilon': 0.1}
SVR_parameter['2N to 1N']['Width'] = {'C': 0.3, 'epsilon': 0.1}
SVR_parameter['2N to 1N']['Weight'] = {'C': 0.01, 'epsilon': 0.2}

SVR_parameter['2P to 1P'] = dict()
SVR_parameter['2P to 1P']['Electricity'] = {'C': 100, 'epsilon': 1.0}
SVR_parameter['2P to 1P']['Moisture'] = {'C': 1e-4, 'epsilon': 0.02}
SVR_parameter['2P to 1P']['Width'] = {'C': 0.3, 'epsilon': 0.1}
SVR_parameter['2P to 1P']['Weight'] = {'C': 0.4, 'epsilon': 0.15}

SVR_parameter['B to 1N'] = dict()
SVR_parameter['B to 1N']['Electricity'] = {'C': 200, 'epsilon': 1.0}
SVR_parameter['B to 1N']['Moisture'] = {'C': 1.0, 'epsilon': 0.01}
SVR_parameter['B to 1N']['Width'] = {'C': 0.3, 'epsilon': 0.1}
SVR_parameter['B to 1N']['Weight'] = {'C': 0.1, 'epsilon': 0.1}

SVR_parameter['B to 1P'] = dict()
SVR_parameter['B to 1P']['Electricity'] = {'C': 100, 'epsilon': 1.0}
SVR_parameter['B to 1P']['Moisture'] = {'C': 0.5, 'epsilon': 0.01}
SVR_parameter['B to 1P']['Width'] = {'C': 0.3, 'epsilon': 0.1}
SVR_parameter['B to 1P']['Weight'] = {'C': 0.4, 'epsilon': 0.1}

