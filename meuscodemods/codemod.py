import libcst as cst
from ast import literal_eval
from libcst.codemod import VisitorBasedCodemodCommand


class IfRemovalCommand(VisitorBasedCodemodCommand):
    DESCRIPTION: str = 'Remove ifs que usem a constante MINHA_FLAG'
    
    def __init(self):
        self.dentro_do_if_a_ser_descartado = False
    
    def leave_Assign(self, original_node, updated_node):
        if 'MINHA_FLAG' in updated_node.targets:
            return RemoveFromParent()
        return updated_node
    
    def visit_If(self, node):
        if node.test.value == 'MINHA_FLAG':
            self.dentro_do_if_a_ser_descartado = True
    
    def leave_If(self, original_node, updated_node):
        if self.dentro_do_if_a_ser_descartado:
            # Evita que outros ifs sejam afetados
            self.dentro_do_if_a_ser_descartado = False
            # Substitui o if pelo conteúdo do bloco dele
            return cst.FlattenSentinel(updated_node.body.body)