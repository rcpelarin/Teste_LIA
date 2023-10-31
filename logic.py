def search(data, filters):
    results = []

    if not filters:
        for curso in data:
            for nivel in data[curso]:
                for turno in data[curso][nivel]:
                    results.extend(data[curso][nivel][turno])
    else:
        curso_filter = filters[0]
        if curso_filter in data:
            if len(filters) == 1:
                for nivel in data[curso_filter]:
                    for turno in data[curso_filter][nivel]:
                        results.extend(data[curso_filter][nivel][turno])
            else:
                nivel_filter = filters[1]
                if nivel_filter in data[curso_filter]:
                    if len(filters) == 2:
                        for turno in data[curso_filter][nivel_filter]:
                            results.extend(data[curso_filter][nivel_filter][turno])
                    else:
                        turno_filter = filters[2]
                        if turno_filter in data[curso_filter][nivel_filter]:
                            results = data[curso_filter][nivel_filter][turno_filter]

    return results
