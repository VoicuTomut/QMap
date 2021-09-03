import numpy as np

from project_qmap.tsp_solutions import get_minim_Brut

def haversine_distance(lat1, lon1, lat2, lon2):
   r = 6371
   phi1 = np.radians(lat1)
   phi2 = np.radians(lat2)
   delta_phi = np.radians(lat2-lat1)
   delta_lambda = np.radians(lon2-lon1)
   a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) *   np.sin(delta_lambda / 2)**2
   res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1-a)))
   return np.round(res, 5)

def clasic_Brut(poz):
    '''

    :param poz:
    :return:
    '''
    nr_places=len(poz)

    w=np.zeros((nr_places,nr_places))
    for i in range (nr_places):
        for j in range(i+1,nr_places):
            w[i][j]=haversine_distance(poz[i][0], poz[i][1], poz[j][0], poz[j][1])
            w[j][i]=haversine_distance(poz[i][0], poz[i][1], poz[j][0], poz[j][1])

    min,rut=get_minim_Brut(w)

    return min, rut