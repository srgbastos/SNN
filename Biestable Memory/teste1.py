from brian2 import *

tau = 10*ms
vrest = -70.0*mV
R = 100*Mohm
eqs = '''
    dv/dt = (-(v-vrest) + R*I)/tau : volt (unless refractory)
    I : amp
'''
neurons = NeuronGroup(1, eqs, threshold = 'v > -60.0*mV', reset = 'v = vrest', refractory = 5*ms, method = 'linear')
neurons.v = vrest
neurons.I = 100*pA

state_mon = StateMonitor(neurons, 'v', record = True)

run (100*ms)

plot(state_mon.t/ms, state_mon.v[0]/mV)
xlabel('Tempo (ms)')
ylabel('Voltagem (mV)')
show()