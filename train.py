import sys
import os
sys.path.append(os.getcwd())

def main():
    args=parser_args()
    train_loader,test_loader=getDataLoader(args)