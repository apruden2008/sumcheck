1. Prover sends the evaluation of the polynomial
2. Verifier evaluates over the boolean hypercube
3. Verifier chooses a random field element and sends to prover, which then "fixes" variable a
4. Iteratvely, the prover and verifier go through this until all of the variables are
   "bound". 
5. Lastly, the verifier performs one evaluation of the full polynomial
