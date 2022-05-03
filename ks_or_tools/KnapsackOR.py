from ortools.algorithms import pywrapknapsack_solver
from itertools import islice
import time
testgroups = ['n00050', 'n00100' , 'n00200', 'n00500', 'n01000']
groupnames = ['00Uncorrelated','01WeaklyCorrelated','02StronglyCorrelated','03InverseStronglyCorrelated', '04AlmostStronglyCorrelated', '05SubsetSum', '06UncorrelatedWithSimilarWeights', '07SpannerUncorrelated', '08SpannerWeaklyCorrelated','09SpannerStronglyCorrelated', '10MultipleStronglyCorrelated','11ProfitCeiling', '12Circle']
for groupname in groupnames:
    for testgroup in testgroups:
       
        filepath = ".\\kplib\\" + groupname + '\\' + testgroup + '\\' + 'R01000' + '\\'

        start = time.time()
        elapsed = 0

        index = 5

        capacities = []
        values = []
        weights = [[]]  
        f = open(filepath + 's00' + str(index) + '.kp')
        lines = f.read().splitlines()

        capacities.append(int(lines[2]))
        for line in islice(lines, 4, None):
            data = line.split()
            values.append(int(data[0]))
            weights[0].append(int(data[1]))

        solver = pywrapknapsack_solver.KnapsackSolver(
            pywrapknapsack_solver.KnapsackSolver.
            KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

        solver.Init(values, weights, capacities)

        #Set time limit - 180 seconds
        #3 minutes = 180 seconds
        solver.set_time_limit(180.0)

        computed_value = solver.Solve()
        packed_items = []
        packed_weights = []
        total_weight = 0

        for i in range(len(values)):
            if solver.BestSolutionContains(i):
                packed_items.append(i)
                packed_weights.append(weights[0][i])
                total_weight += weights[0][i]

        elapsed = time.time() - start

        with open('result.txt', 'a') as a:
            a.write('\nSolution for: '+ groupname + '\\' + testgroup)
            a.write('\nExecution time: {} sec'.format(elapsed))
            a.write('\nCapacity = {} '.format(str(capacities[0])))
            a.write('\nTotal weight: '+ str(total_weight))
            a.write('\nTotal value: '+ str(computed_value))
            a.write('\nNumber of items: {} '.format(str(len(packed_items))))
            a.write('\nPacked weights: {}'.format(len(packed_weights)))
            a.write('\nPacked items: {} \n'.format(packed_items))
            a.write('-------------------------')
            
        print('Group: ' + groupname + ' | ' + 'Size: ' + testgroup + ' completed')
    a.close()  
    