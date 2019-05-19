import torch
import torch.nn as nn
import imp
import os


current_path = os.path.abspath(__file__)
filepath_to_classifier_definition = os.path.join(os.path.dirname(current_path), 'NonLinearClassifier.py')
NonLinearClassifier = imp.load_source('',filepath_to_classifier_definition).create_model


class MClassifier(nn.Module):
    def __init__(self, opts):
        super(MClassifier, self).__init__()
        #print('Number of classifiers: ',len(opts))
        self.classifiers = nn.ModuleList([NonLinearClassifier(opt) for opt in opts])
        self.num_classifiers = len(opts)


    def forward(self, feats):
        #print('feats: ',len(feats))
        #print('self.classifiers',self.num_classifiers)
        assert(len(feats) == self.num_classifiers)
        return [self.classifiers[i](feat) for i, feat in enumerate(feats)]


def create_model(opt):
    return MClassifier(opt)