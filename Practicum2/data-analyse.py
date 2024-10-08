import numpy as np
import matplotlib.pyplot as plt

def main(SHOW):
    #INFO: lengtes en lengtecheck
    R = np.array([470, 680, 750, 1000, 1500, 2400])
    VK_1 = np.array([4.65, 4.70, 4.71, 4.74, 4.77, 4.79])
    VK_2 = np.array([10.13, 10.46, 10.54, 10.71, 10.90, 11.05])

    VE_1 = 4.82
    VE_2 = 11.30

    resolutie = 0.01
    naukeurigheid = 0.01

    if len(R) != len(VK_1) or len(R) != len(VK_2):
        raise "Lengtes komen niet overeen"

    #INFO: analyse
    E_R = naukeurigheid*R

    E_VE_1 = (naukeurigheid + resolutie*VE_1)/2
    E_VE_2 = (naukeurigheid + resolutie*VE_2)/2

    E_VK_1 = (naukeurigheid + resolutie*VK_1)/2
    E_VK_2 = (naukeurigheid + resolutie*VK_2)/2

    Ri_1 = R * (VE_1 / VK_1 - 1)
    Ri_2 = R * (VE_2 / VK_2 - 1)
    E_Ri_1 = np.sqrt( (VE_1/VK_1 - 1)**2 * (E_R)**2 + (R**2/VK_1**2)*E_VE_1**2 + (VE_1**2 * R**2 / VK_1**4) * E_VK_1**2)
    E_Ri_2 = np.sqrt( (VE_2/VK_2 - 1)**2 * (E_R)**2 + (R**2/VK_2**2)*E_VE_2**2 + (VE_2**2 * R**2 / VK_2**4) * E_VK_2**2)

    #G_Ri_1 = (1/len(Ri_1))*np.sum(Ri_1) 
    #G_Ri_1_B1 = (1/len(Ri_1))*np.sum(Ri_1) #FIXME: waarom i=2 als alle resultaten, pak alles behalve 1ste Ri_1[:1]
    #E_G_Ri_1 = np.sqrt((1/(len(Ri_1)-1))*np.sum((Ri_1 - G_Ri_1_B1)**2)) #/np.sqrt(len(Ri_1))#TODO: delen door wortel N?
    G_Ri_1 = np.sum(((1/(E_Ri_1))**2)*Ri_1)/np.sum(((1/(E_Ri_1))**2))
    E_G_Ri_1 = 1/np.sqrt(np.sum(((1/(E_Ri_1))**2)))

    #G_Ri_2 = (1/len(Ri_2))*np.sum(Ri_2) 
    #G_Ri_2_B1 = (1/len(Ri_2))*np.sum(Ri_2) #FIXME: waarom i=2 als alle resultaten, pak alles behalve 1ste Ri_1[:1]
    #E_G_Ri_2 = np.sqrt((1/(len(Ri_2)-1))*np.sum((Ri_2 - G_Ri_2_B1)**2)) #/np.sqrt(len(Ri_2))#TODO: delen door wortel N?
    G_Ri_2 = np.sum(((1/(E_Ri_2))**2)*Ri_2)/np.sum(((1/(E_Ri_2))**2))
    E_G_Ri_2 = 1/np.sqrt(np.sum(((1/(E_Ri_2))**2)))
    

    #INFO: plot
    def plot(R, Ri_1, E_Ri_1):
        plt.plot(R, Ri_1, marker='o', linestyle='None', label='Ri_1', color='blue')
        plt.errorbar(R, Ri_1, yerr=E_Ri_1, fmt='o', label='Ri_1', color='blue', capsize=5)

        # Adding labels and title
        plt.xlabel('R Values')
        plt.ylabel('Ri Values')
        plt.title('Line Plot of Ri_1 and error')
        plt.legend()

        # Show the plot
        plt.show()

    #INFO: SHOW
    if SHOW:
        print(" ")
        #print(VK_1)
        #print(E_VK_1)
        #print("---------")
        #print(VK_2)
        #print(E_VK_2)
        #print("---------")
        #print(VE_1)
        #print(E_VE_1)
        #print("---------")
        #print(VE_2)
        #print(E_VE_2)
        #print("---------")
        #print('Ri_1')
        #print(Ri_1)
        #print(E_Ri_1)
        #print("---------")
        #print('Ri_2')
        #print(Ri_2)
        #print(E_Ri_2)
        #print("---------")
        print('G_Ri_1')
        print(G_Ri_1)
        print(E_G_Ri_1)
        print("---------")
        print('G_Ri_2')
        print(G_Ri_2)
        print(E_G_Ri_2)




if __name__ == "__main__":
    SHOW = True
    print("---------START---------")
    main(SHOW)
    print("----------END----------")
