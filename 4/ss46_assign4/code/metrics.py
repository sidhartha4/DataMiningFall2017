import sys
import csv

def main(fileName):

    fo = open(fileName, "r")

    line = fo.readlines()

    confusion_matrix = []
    
    for i in line:
        i = i.rstrip()
        j = i.split(" ")
        inList = []
        for k in j:
            inList.append(int(k))
        confusion_matrix.append(inList)


    print(confusion_matrix)
    
    n = len(confusion_matrix)

    acc = 0
    total = sum([sum(i) for i in confusion_matrix])
    for i in range(n):
        acc += confusion_matrix[i][i]
    print ("Total:", total)
    ovacc = acc/total
    print ("Overall Accuracy:", ovacc)

    printList = []
    printList.append(["",""])
    printList.append([fileName, ""])
    printList.append(["Overall Accuracy:", ovacc])


    for i in range(n):
        printList.append(["",""])
        
        printList.append(["Class: "+ str(i+1) ,""])
        print ("IDX: ", i)
        # Accuracy, Specificity, Precision, Recall, F-1 Score, F \beta score (\beta = 0.5 and 2)
        tp, fp, tn, fn = 0, 0, 0, 0
        p = sum(confusion_matrix[i])
        neg = total - p
        tp = confusion_matrix[i][i]
        # print ("TP", tp)
        row = confusion_matrix[i][::]
        del row[i]
        # print ("FN", row)
        fn = sum(row)
        col = [j[i] for j in confusion_matrix][::]
        del col[i]
        # print ("FP", col)
        fp = sum(col)

        for j in range(n):
            for k in range(n):
                if j !=i and k != i:
                    # print ("tn", confusion_matrix[j][k])
                    tn += confusion_matrix[j][k]

        
        
        try:
            val = (tp + tn) / (p + neg)
            print (i+1, "Accuracy:", val )
            printList.append(["Accuracy", val])
        except ZeroDivisionError:
            print (i+1, "Accuracy:", float('inf'))
            printList.append(["Accuracy", float('inf')])
        
        try:
            val = (tn) / (neg) 
            print (i+1, "Specificity:", val)
            printList.append(["Specificity", val])
        except ZeroDivisionError:
            print (i+1, "Specificity:", float('inf') )
            printList.append(["Specificity:", float('inf')])
        
        try:
            precision = (tp) / (tp + fp)
            print (i+1, "Precision:",  precision)
            printList.append(["Precision", precision])
        
        except ZeroDivisionError:
            precision = float('inf')
            print (i+1, "Precision:",  float('inf'))
            printList.append(["Precision:",  float('inf')])
        
        try:
            recall = (tp) / (p)
            print (i+1, "Recall:",  recall)
            printList.append(["Recall", recall])
        except ZeroDivisionError:
            recall = float('inf')
            print (i+1, "Recall:",  float('inf'))
            printList.append(["Recall:",  float('inf')])

        try: 
            val = (2 * precision * recall) / (precision + recall) 
            print (i+1, "F1-score:", val)
            printList.append(["F1-score", recall])

        except ZeroDivisionError:
            print (i+1, "F1-score:", float('inf'))
            printList.append(["F1-score:", float('inf')])

        try:
            val = ( (1 + (0.5**2)) * precision * recall) / ( ((0.5 ** 2) * precision) + recall) 
            print (i+1, "F / 0.5:", val)
            printList.append(["F / 0.5", val])
        except ZeroDivisionError:
            print (i+1, "F / 0.5:", float('inf'))
            printList.append(["F / 0.5:", float('inf')])
        
        try:
            val = ( (1 + (2**2)) * precision * recall) / ( ((2 ** 2) * precision) + recall) 
            print (i+1, "F / 2: ", val)
            printList.append(["F / 2", val])
        except ZeroDivisionError:
            print (i+1, "F / 2: ", float('inf'))
            printList.append(["F / 2: ", float('inf')])

    with open("output.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerows(printList)

if __name__ == '__main__':
    file1 = sys.argv[1]
    main(file1)
    """
    file2 = sys.argv[2]
    main(file2)
    file3 = sys.argv[3]
    main(file3)
    file4 = sys.argv[4]
    main(file4)
    """ 