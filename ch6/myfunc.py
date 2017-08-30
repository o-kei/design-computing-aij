def inherit_get(DG, gparent, parent):
    # parent の下にリンクがあるかを判定
    if DG.successors(parent):
        for child in DG.successors(parent):
            # child の下にリンクがあるかを判定
            if DG.successors(child):
                # parent と child 間の関係が is_a かどうかを判定
                if DG.edge[parent][child]['type'] == 'is_a':
                    # is_a の場合は，さらにそのリンクをたどる
                    inherit_get(DG, gparent, child)
                else:
                    # parent と child の関係を出力する
                    print(gparent, DG.edge[parent][child]['type'], child)
            else:
                # gparent と child の関係を出力する
                print(gparent, DG.edge[parent][child]['type'], child)
    else:
        print('No inheritance available.')
