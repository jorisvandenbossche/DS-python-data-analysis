class Employee():  #object
    
    def __init__(self, name, wage=60.):
        """
        Employee class to save the amount of hours worked and related earnings
        """
        self.name = name
        self.wage = wage
        self.projects = {}  

    def new_project(self, projectname):
        """
        """
        if projectname in self.projects:
            raise Exception("project already exist for", self.name)
        else:
            self.projects[projectname] = 0.
            
        
    def worked(self, hours, projectname):
        """add worked hours on a project
        """
        try:
            hours = float(hours)
        except:
            raise Exception("Hours not convertable to float!")

        if not projectname in self.projects:
            raise Exception("project non-existing for", self.name)
            
        self.projects[projectname] += hours
        
    def calc_earnings(self):
        """
        Calculate earnings
        """
        total_hours = 0
        for val in self.projects.values():
            total_hours += val
            
        return total_hours *self.wage
    
    def info(self):
        """
        get info
        """
        for proj, hour in self.projects.items():
            print(hour, 'worked on project', proj)